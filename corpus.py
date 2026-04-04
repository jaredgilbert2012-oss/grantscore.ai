# ============================================================
# GrantScore AI — Corpus
# Funded and unfunded grant abstracts for model comparison
# ============================================================
# INSTRUCTIONS:
#   - Add real NIH Reporter abstracts between the triple quotes
#   - Keep each abstract as one continuous text block
#   - Aim for 8-10 funded, 4-6 unfunded examples
#   - Label each with source info in the comment above it
#   - Agency/mechanism noted for future multi-corpus expansion
#
# SOURCE: NIH Reporter (reporter.nih.gov)
# DOMAIN: Neuroscience / Mental Health
# MECHANISM: R01
# ============================================================

# ── FUNDED EXAMPLES ─────────────────────────────────────────
# These abstracts represent successfully funded R01 applications
# exhibiting strong preliminary data, mechanistic clarity,
# investigator credentials, and explicit gap statements.

# ── TIER 1: Strong funded (top decile, scores ~10–18 percentile) ──
strong_funded = [
    """...""",
]

# ── TIER 2: Borderline funded (payline edge, scores ~19–28 percentile) ──
borderline_funded = [
    """...""",
]

# ── TIER 3: Constructed weak examples (illustrative low-scoring) ──
# Replace with real unfunded abstracts once data partnership is active
weak_examples = [
    """...""",
]

# Combined lists used by the app
funded_examples   = strong_funded + borderline_funded
unfunded_examples = weak_examples

# ── UNFUNDED / WEAK EXAMPLES ─────────────────────────────────
# These abstracts represent applications that were not funded
# or scored poorly. Use anonymized real examples where possible,
# or well-constructed weak examples that illustrate common gaps.

unfunded_examples = [

    # [1] Weak example — vague significance, no preliminary data
    """
    Mental health is increasingly recognized as important. This project
    will investigate stress in college students using surveys and interviews.
    Students will complete questionnaires about their stress levels and we
    will analyze the results. We hope to find out what causes stress and
    what might help. The findings will be useful for universities trying
    to support student wellbeing.
    """,

    # [2] Weak example — no mechanistic rationale, no credentials
    """
    Depression affects many people and is a serious problem. We want to
    understand what causes depression and how we can help people who suffer
    from it. We will recruit patients from local clinics and give them
    questionnaires. Our team is interested in this area and has been
    working on mental health topics for several years. We believe this
    research will be significant and publishable.
    """,

    # [3] Weak example — generic methods, no gap statement
    """
    Anxiety disorders are common in the United States. This study will
    examine whether therapy helps people with anxiety feel better. We will
    compare two groups of patients over six months and measure their
    anxiety levels before and after treatment. Results will contribute to
    the literature on anxiety treatment and inform clinical practice.
    """,

]
