# ============================================================
# embed_corpus.py — GrantScore AI Stage 2
# ============================================================
# PURPOSE:
#   One-time script to embed all corpus abstracts into vectors
#   and upload them to Pinecone with metadata for filtered retrieval.
#
# WHEN TO RUN:
#   - First time setting up Stage 2
#   - Any time you add new abstracts to corpus.py
#   - Run locally (Terminal or Colab) — NOT part of the Streamlit app
#
# PREREQUISITES:
#   pip3 install anthropic pinecone voyageai
#   Pinecone index created at pinecone.io with:
#     - Dimensions: 1024  (voyage-3 outputs 1024 dimensions)
#     - Metric: cosine
#     - Name: grantscore-corpus (or update INDEX_NAME below)
#
# ENVIRONMENT VARIABLES REQUIRED (set in terminal before running):
#   export ANTHROPIC_API_KEY="sk-ant-..."
#   export PINECONE_API_KEY="..."
#   export VOYAGE_API_KEY="pa-..."
#
# USAGE:
#   python3 embed_corpus.py
# ============================================================

import os
import anthropic
import voyageai
from pinecone import Pinecone
from corpus import funded_corpus, unfunded_corpus

# ── Configuration ─────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
PINECONE_API_KEY  = os.environ.get("PINECONE_API_KEY", "")
VOYAGE_API_KEY    = os.environ.get("VOYAGE_API_KEY", "")
INDEX_NAME        = "grantscore-corpus"

# ── Connect to services ───────────────────────────────────────
print("Connecting to services...")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
vo     = voyageai.Client(api_key=VOYAGE_API_KEY)
pc     = Pinecone(api_key=PINECONE_API_KEY)
index  = pc.Index(INDEX_NAME)

print(f"Connected. Current index size: "
      f"{index.describe_index_stats()['total_vector_count']} vectors\n")

# ── Embedding function ────────────────────────────────────────
def get_embedding(text):
    """
    Convert a text abstract into a vector using Voyage AI's
    voyage-3 model. input_type="document" is used for corpus
    items being stored. Use input_type="query" in retriever.py
    for the incoming grant draft being searched.
    """
    response = vo.embed(
        [text.strip()],
        model="voyage-3",
        input_type="document"
    )
    return response.embeddings[0]


# ── Upload function ───────────────────────────────────────────
def embed_and_upload(corpus, label):
    """
    Embed each abstract and upload to Pinecone with full metadata.

    Parameters:
        corpus (list of dicts): funded_corpus or unfunded_corpus
        label  (str):           "funded" or "unfunded"
    """
    vectors = []

    for i, entry in enumerate(corpus, 1):
        pi_name = entry.get("pi", "unknown")
        print(f"  Embedding {label} example {i}/{len(corpus)}: {pi_name} ...")

        embedding = get_embedding(entry["text"])

        metadata = {
            "text":          entry["text"].strip(),
            "label":         entry.get("label", label),
            "tier":          entry.get("tier", "unknown"),
            "institution":   entry.get("institution", "unknown"),
            "study_section": entry.get("study_section", "unknown"),
            "fiscal_year":   str(entry.get("fiscal_year", "unknown")),
            "source":        entry.get("source", "unknown"),
            "pi":            entry.get("pi", "unknown"),
            "award_amount":  entry.get("award_amount", 0),
            "notes":         entry.get("notes", "")
        }

        vector_id = f"{label}-{i:03d}"

        vectors.append({
            "id":       vector_id,
            "values":   embedding,
            "metadata": metadata
        })

    print(f"\n  Uploading {len(vectors)} {label} vectors to Pinecone...")
    index.upsert(vectors=vectors)
    print(f"  ✅ {label.capitalize()} examples uploaded successfully.\n")

    return len(vectors)


# ── Main execution ────────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 60)
    print("  GrantScore AI — Corpus Embedding Script")
    print("=" * 60)
    print(f"\nCorpus summary:")
    print(f"  Funded examples:   {len(funded_corpus)}")
    print(f"  Unfunded examples: {len(unfunded_corpus)}")
    print(f"  Total to embed:    {len(funded_corpus) + len(unfunded_corpus)}")
    print()

    print("── Funded examples ─────────────────────────────────────")
    funded_count = embed_and_upload(funded_corpus, "funded")

    print("── Unfunded examples ───────────────────────────────────")
    unfunded_count = embed_and_upload(unfunded_corpus, "unfunded")

    final_stats = index.describe_index_stats()
    total = final_stats['total_vector_count']

    print("=" * 60)
    print(f"  Done! Index now contains {total} vectors.")
    print(f"  Funded:   {funded_count}")
    print(f"  Unfunded: {unfunded_count}")
    print()
    print("  Next step: build and run retriever.py.")
    print("=" * 60)
