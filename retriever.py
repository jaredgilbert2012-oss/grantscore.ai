# ============================================================
# retriever.py — GrantScore AI Stage 2
# ============================================================
# PURPOSE:
#   Given a new grant abstract, find the most semantically
#   similar funded and unfunded examples from the Pinecone
#   vector database.
#
# KEY DESIGN: Keys are read lazily inside get_clients() rather
#   than at module load time. This is critical for Streamlit
#   Cloud, where st.secrets is only available after the app
#   starts — not at import time.
#
# USAGE:
#   Imported by grantscore_app.py:
#     from retriever import retrieve_similar
#     funded_texts, unfunded_texts = retrieve_similar(draft_text)
#
#   Standalone test:
#     python3 retriever.py
# ============================================================

import os

INDEX_NAME = "grantscore-corpus"

# ── Key resolution ────────────────────────────────────────────
def _get_key(name):
    """
    Read a key from environment variables first, then fall back
    to Streamlit secrets. Trying st.secrets at module load time
    fails on Streamlit Cloud — this defers the read until the
    function is actually called, by which time secrets are ready.
    """
    # Check environment variable first (local dev)
    value = os.environ.get(name, "")
    if value:
        return value

    # Fall back to Streamlit secrets (Streamlit Cloud)
    try:
        import streamlit as st
        return st.secrets.get(name, "")
    except Exception:
        return ""


# ── Lazy client initialisation ────────────────────────────────
_vo    = None
_index = None

def get_clients():
    """
    Initialise Voyage AI and Pinecone clients on first call.
    Reuses existing clients on subsequent calls (singleton pattern).
    Reading keys here rather than at module level ensures
    st.secrets is available when this runs on Streamlit Cloud.
    """
    global _vo, _index

    if _vo is None or _index is None:
        import voyageai
        from pinecone import Pinecone

        pinecone_key = _get_key("PINECONE_API_KEY")
        voyage_key   = _get_key("VOYAGE_API_KEY")

        if not pinecone_key or not voyage_key:
            raise ValueError(
                "PINECONE_API_KEY and VOYAGE_API_KEY must be set. "
                "Export them as environment variables or add them to "
                "Streamlit secrets."
            )

        _vo    = voyageai.Client(api_key=voyage_key)
        pc     = Pinecone(api_key=pinecone_key)
        _index = pc.Index(INDEX_NAME)

    return _vo, _index


# ── Embedding function ────────────────────────────────────────
def get_query_embedding(text):
    """
    Embed an incoming grant draft for similarity search.
    input_type="query" is optimised for search queries
    (vs "document" used in embed_corpus.py for storage).
    """
    vo, _ = get_clients()
    response = vo.embed(
        [text.strip()],
        model="voyage-3",
        input_type="query"
    )
    return response.embeddings[0]


# ── Core retrieval function ───────────────────────────────────
def retrieve_similar(draft_text, n_funded=5, n_unfunded=3):
    """
    Given a grant draft, retrieve the most semantically similar
    funded and unfunded examples from the Pinecone index.

    Parameters:
        draft_text  (str): The grant abstract or specific aims
        n_funded    (int): Number of funded examples to retrieve
        n_unfunded  (int): Number of unfunded examples to retrieve

    Returns:
        funded_texts   (list of str): Most similar funded abstracts
        unfunded_texts (list of str): Most similar unfunded abstracts
    """
    _, index = get_clients()

    query_vector = get_query_embedding(draft_text)

    funded_results = index.query(
        vector=query_vector,
        top_k=n_funded,
        filter={"label": {"$eq": "funded"}},
        include_metadata=True
    )

    unfunded_results = index.query(
        vector=query_vector,
        top_k=n_unfunded,
        filter={"label": {"$eq": "unfunded"}},
        include_metadata=True
    )

    funded_texts = [
        match["metadata"]["text"]
        for match in funded_results["matches"]
    ]

    unfunded_texts = [
        match["metadata"]["text"]
        for match in unfunded_results["matches"]
    ]

    return funded_texts, unfunded_texts


# ── Retrieval with metadata (debugging) ──────────────────────
def retrieve_similar_with_metadata(draft_text, n_funded=5, n_unfunded=3):
    """
    Same as retrieve_similar() but also returns similarity scores
    and metadata. Used for debugging and the standalone test below.
    """
    _, index = get_clients()

    query_vector = get_query_embedding(draft_text)

    funded_results = index.query(
        vector=query_vector,
        top_k=n_funded,
        filter={"label": {"$eq": "funded"}},
        include_metadata=True
    )

    unfunded_results = index.query(
        vector=query_vector,
        top_k=n_unfunded,
        filter={"label": {"$eq": "unfunded"}},
        include_metadata=True
    )

    funded_matches = [
        {
            "text":   match["metadata"]["text"],
            "score":  round(match["score"], 4),
            "pi":     match["metadata"].get("pi", "unknown"),
            "source": match["metadata"].get("source", "unknown"),
            "tier":   match["metadata"].get("tier", "unknown"),
            "notes":  match["metadata"].get("notes", "")
        }
        for match in funded_results["matches"]
    ]

    unfunded_matches = [
        {
            "text":  match["metadata"]["text"],
            "score": round(match["score"], 4),
            "notes": match["metadata"].get("notes", "")
        }
        for match in unfunded_results["matches"]
    ]

    return funded_matches, unfunded_matches


# ── Standalone test ───────────────────────────────────────────
if __name__ == "__main__":

    TEST_ABSTRACT = """
    Anxiety disorders affect approximately 31% of young adults in the
    United States, yet access to scalable, evidence-based interventions
    remains limited. This study will evaluate the efficacy of a 6-week
    mobile-based cognitive behavioral therapy (CBT) intervention designed
    to reduce generalized anxiety symptoms among young adults aged 18-25.
    We will conduct a randomized controlled trial (N = 200) comparing the
    intervention to a waitlist control group. Primary outcomes will include
    changes in anxiety severity measured by the GAD-7. Data will be analyzed
    using mixed-effects regression models to account for repeated measures.
    """

    print("=" * 60)
    print("  GrantScore AI — Retriever Test")
    print("=" * 60)
    print(f"\nTest abstract (truncated):")
    print(f"  '{TEST_ABSTRACT.strip()[:100]}...'\n")

    print("Retrieving similar examples from Pinecone...")
    funded_matches, unfunded_matches = retrieve_similar_with_metadata(
        TEST_ABSTRACT,
        n_funded=5,
        n_unfunded=3
    )

    print("\n── Top funded matches ───────────────────────────────────")
    for i, match in enumerate(funded_matches, 1):
        print(f"\n  [{i}] Similarity score: {match['score']}")
        print(f"      PI:     {match['pi']}")
        print(f"      Source: {match['source']}")
        print(f"      Notes:  {match['notes']}")
        print(f"      Text:   {match['text'][:120].strip()}...")

    print("\n── Top unfunded matches ─────────────────────────────────")
    for i, match in enumerate(unfunded_matches, 1):
        print(f"\n  [{i}] Similarity score: {match['score']}")
        print(f"      Notes: {match['notes']}")
        print(f"      Text:  {match['text'][:120].strip()}...")

    print("\n" + "=" * 60)
    print("  Retriever working correctly if scores > 0.0")
    print("  Higher scores = more similar to your test abstract")
    print("  Funded matches should feel thematically related")
    print("=" * 60)
