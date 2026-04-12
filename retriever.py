# ============================================================
# retriever.py — GrantScore AI Stage 2
# ============================================================
# PURPOSE:
#   Given a new grant abstract, find the most semantically
#   similar funded and unfunded examples from the Pinecone
#   vector database. These replace the hardcoded corpus lists
#   in grantscore_app.py for dynamic, context-aware retrieval.
#
# HOW IT WORKS:
#   1. Embed the incoming grant draft using voyage-3
#      (input_type="query" for search, vs "document" for storage)
#   2. Query Pinecone separately for funded and unfunded matches
#   3. Return the top-N most similar abstracts as plain strings
#      ready to drop into the existing build_prompt() function
#
# USAGE:
#   Imported by grantscore_app.py:
#     from retriever import retrieve_similar
#     funded_texts, unfunded_texts = retrieve_similar(draft_text)
#
#   Can also be tested standalone:
#     python3 retriever.py
#
# ENVIRONMENT VARIABLES REQUIRED:
#   export PINECONE_API_KEY="..."
#   export VOYAGE_API_KEY="pa-..."
#   (ANTHROPIC_API_KEY not needed here — retriever uses Voyage only)
# ============================================================

import os
import voyageai
import streamlit as st
from pinecone import Pinecone

# ── Configuration ─────────────────────────────────────────────
# Read keys from environment or Streamlit secrets
try:
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY") or st.secrets.get("PINECONE_API_KEY", "")
    VOYAGE_API_KEY   = os.environ.get("VOYAGE_API_KEY")   or st.secrets.get("VOYAGE_API_KEY", "")
except Exception:
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY", "")
    VOYAGE_API_KEY   = os.environ.get("VOYAGE_API_KEY", "")
INDEX_NAME       = "grantscore-corpus"

# ── Connect to services ───────────────────────────────────────
vo    = voyageai.Client(api_key=VOYAGE_API_KEY)
pc    = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)


# ── Embedding function ────────────────────────────────────────
def get_query_embedding(text):
    """
    Embed an incoming grant draft for similarity search.
    Uses input_type="query" which is optimised for search
    (vs "document" used in embed_corpus.py for storage).
    Using the correct input_type improves retrieval accuracy.
    """
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

    Usage in grantscore_app.py:
        funded_texts, unfunded_texts = retrieve_similar(draft_text)
    """
    # Step 1 — Embed the incoming draft as a search query
    query_vector = get_query_embedding(draft_text)

    # Step 2 — Find most similar funded examples
    funded_results = index.query(
        vector=query_vector,
        top_k=n_funded,
        filter={"label": {"$eq": "funded"}},
        include_metadata=True
    )

    # Step 3 — Find most similar unfunded examples
    unfunded_results = index.query(
        vector=query_vector,
        top_k=n_unfunded,
        filter={"label": {"$eq": "unfunded"}},
        include_metadata=True
    )

    # Step 4 — Extract text from results
    # Returns plain strings ready for build_prompt()
    funded_texts = [
        match["metadata"]["text"]
        for match in funded_results["matches"]
    ]

    unfunded_texts = [
        match["metadata"]["text"]
        for match in unfunded_results["matches"]
    ]

    return funded_texts, unfunded_texts


# ── Retrieval with metadata (for debugging/logging) ───────────
def retrieve_similar_with_metadata(draft_text, n_funded=5, n_unfunded=3):
    """
    Same as retrieve_similar() but also returns match scores
    and metadata. Useful for debugging and understanding which
    corpus examples are being selected and why.

    Returns:
        funded_matches   (list of dicts): {text, score, pi, source, ...}
        unfunded_matches (list of dicts): {text, score, notes, ...}
    """
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
            "text":    match["metadata"]["text"],
            "score":   round(match["score"], 4),
            "pi":      match["metadata"].get("pi", "unknown"),
            "source":  match["metadata"].get("source", "unknown"),
            "tier":    match["metadata"].get("tier", "unknown"),
            "notes":   match["metadata"].get("notes", "")
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
    """
    Test the retriever with a sample grant abstract.
    Run: python3 retriever.py
    """

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
