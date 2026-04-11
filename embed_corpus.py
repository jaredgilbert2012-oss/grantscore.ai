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
#   pip install anthropic pinecone-client
#   Pinecone index created at pinecone.io with:
#     - Dimensions: 1536
#     - Metric: cosine
#     - Name: grantscore-corpus (or update INDEX_NAME below)
#
# USAGE:
#   python embed_corpus.py
#
# EXPECTED OUTPUT:
#   Embedding funded example 1/8: Bennett, David A. ...
#   Embedding funded example 2/8: Williams, Paige L. et al. ...
#   ...
#   Uploading 8 funded vectors to Pinecone...
#   Uploading 4 unfunded vectors to Pinecone...
#   Done! Total vectors in index: 12
# ============================================================

import anthropic
from pinecone import Pinecone
import os

# ── Configuration ─────────────────────────────────────────────
# Replace with your actual keys before running.
# Never commit real keys to GitHub — use environment variables
# in production (os.environ.get("ANTHROPIC_API_KEY"))

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
PINECONE_API_KEY  = os.environ.get("PINECONE_API_KEY", "")
INDEX_NAME        = "grantscore-corpus"

# ── Corpus import ─────────────────────────────────────────────
# Imports the full dict lists (not the flat text lists)
# corpus.py must be in the same directory as this script

from corpus import funded_corpus, unfunded_corpus

# ── Connect to services ───────────────────────────────────────
print("Connecting to Anthropic and Pinecone...")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
pc     = Pinecone(api_key=PINECONE_API_KEY)
index  = pc.Index(INDEX_NAME)

print(f"Connected. Current index size: "
      f"{index.describe_index_stats()['total_vector_count']} vectors\n")

# ── Embedding function ────────────────────────────────────────
def get_embedding(text):
    """
    Convert a text abstract into a 1536-dimensional vector
    using Anthropic's voyage-3 embedding model.
    """
   import voyageai
    vo = voyageai.Client(api_key=os.environ.get("VOYAGE_API_KEY", ""))
    response = vo.embed(
        [text.strip()],
        model="voyage-3",
        input_type="document"
    )
    return response.embeddings[0]


# ── Upload function ───────────────────────────────────────────
def embed_and_upload(corpus, label):
    """
    Embed each abstract in the corpus and upload to Pinecone
    with full metadata for Stage 2 filtered retrieval.

    Parameters:
        corpus (list of dicts): funded_corpus or unfunded_corpus
        label  (str):           "funded" or "unfunded"
    """
    vectors = []

    for i, entry in enumerate(corpus, 1):
        pi_name = entry.get("pi", "unknown")
        print(f"  Embedding {label} example {i}/{len(corpus)}: {pi_name} ...")

        # Get the vector for this abstract
        embedding = get_embedding(entry["text"])

        # Build the metadata dict — all fields available for
        # Pinecone filtered retrieval in Stage 2
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

        # Pinecone vector ID — label + index for easy identification
        vector_id = f"{label}-{i:03d}"

        vectors.append({
            "id":       vector_id,
            "values":   embedding,
            "metadata": metadata
        })

    # Upload all vectors for this label in one batch
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

    # Embed and upload funded examples
    print("── Funded examples ─────────────────────────────────────")
    funded_count = embed_and_upload(funded_corpus, "funded")

    # Embed and upload unfunded examples
    print("── Unfunded examples ───────────────────────────────────")
    unfunded_count = embed_and_upload(unfunded_corpus, "unfunded")

    # Final verification
    final_stats = index.describe_index_stats()
    total = final_stats['total_vector_count']

    print("=" * 60)
    print(f"  Done! Index now contains {total} vectors.")
    print(f"  Funded:   {funded_count}")
    print(f"  Unfunded: {unfunded_count}")
    print()
    print("  Next step: run retriever.py to test similarity search.")
    print("=" * 60)
