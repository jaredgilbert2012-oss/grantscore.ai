"""
GrantScore AI — Web UI v0.3 (Stage 2)
Built with Streamlit

Changes in v0.3:
  - Stage 2 RAG enabled: dynamic retrieval from Pinecone
  - Corpus examples now selected by semantic similarity to input
  - Falls back to static corpus if retriever unavailable
  - Retrieval mode shown in report caption

To run locally:
    pip install streamlit anthropic voyageai pinecone
    streamlit run grantscore_app.py

Environment variables required for Stage 2 retrieval:
    export PINECONE_API_KEY="..."
    export VOYAGE_API_KEY="pa-..."

To share:
    Deploy free at share.streamlit.io
    Set PINECONE_API_KEY and VOYAGE_API_KEY in Streamlit secrets
"""

import os
import streamlit as st
import anthropic

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="GrantScore AI",
    page_icon="🎯",
    layout="centered"
)

# ── Header ───────────────────────────────────────────────────
st.title("🎯 GrantScore AI")
st.caption("Predictive grant scoring powered by historical outcome data.")
st.divider()

# ── Stage 2: Dynamic retrieval setup ─────────────────────────
# Attempt to load the retriever. If Pinecone/Voyage keys are not
# available (e.g. Streamlit Cloud without secrets set), falls back
# gracefully to the static corpus so the app never breaks.

STAGE2_AVAILABLE = False

try:
    from retriever import retrieve_similar
    pinecone_key = os.environ.get("PINECONE_API_KEY") or st.secrets.get("PINECONE_API_KEY", "")
    voyage_key   = os.environ.get("VOYAGE_API_KEY")   or st.secrets.get("VOYAGE_API_KEY", "")

if pinecone_key and voyage_key:
    STAGE2_AVAILABLE = True

except Exception:
    pass

# Static corpus fallback (Stage 1 behavior)
if not STAGE2_AVAILABLE:
    from corpus import funded_examples_text, unfunded_examples_text

# ── NIH Rubric ───────────────────────────────────────────────
NIH_RUBRIC = """
SCORING FRAMEWORK — NIH Peer Review Criteria
Reviewers evaluate five criteria, each scored 1 (exceptional) to 9 (poor):

1. SIGNIFICANCE — Does this address an important problem or critical barrier?
   Funded hallmarks: quantified disease burden, explicit gap statement,
   consequences if aims not achieved clearly stated.

2. INNOVATION — Does it challenge existing paradigms or develop new methodologies?
   Funded hallmarks: explicitly states what has never been done before,
   references prior art and explains how this advances beyond it.

3. APPROACH — Are the design, methods, and analyses rigorous and feasible?
   Funded hallmarks: specific sample sizes with power calculations, named
   validated instruments, defined statistical analysis plan, acknowledged
   limitations with mitigation strategies.

4. INVESTIGATORS — Are the PIs and collaborators well-suited to this project?
   Funded hallmarks: years of relevant experience stated, publication count
   or patents cited, prior NIH funding history by grant number, complementary
   team composition described.

5. ENVIRONMENT — Does the institutional environment contribute to success?
   Funded hallmarks: core facilities named, institutional support mentioned,
   collaborating sites identified for multi-site studies, existing cohorts
   or infrastructure leveraged.

NOTE: Following NIH convention — lower scores = stronger application.
Score of 10 = exceptional (top 10%), 50 = average, 90 = poor.

SCALE CALIBRATION: Consider the mechanism type when applying corpus
comparisons. A well-designed R21 exploratory application should not be
penalized for lacking the infrastructure of a multi-site R01 cohort study.
Score relative to what is appropriate and achievable for the stated mechanism.

PROFILE-ABSTRACT CONSISTENCY: When an investigator profile is provided,
assess whether the abstract reflects it. Strong investigators who fail to
reference their preliminary data, prior funding, or institutional resources
in the abstract are missing a significant opportunity — note this explicitly
as a presentation gap rather than a scientific gap.
"""

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        help="Get yours at console.anthropic.com"
    )

    st.divider()
    st.subheader("Application Context")

    agency = st.selectbox(
        "Funding Agency",
        ["NIH", "NSF", "DOD", "Foundation / Private"],
        index=0
    )

    mechanism = st.selectbox(
        "Grant Mechanism",
        ["R01", "R21", "R03", "K-Award", "CAREER", "General"],
        index=0
    )

    institution_type = st.selectbox(
        "Institution Type",
        [
            "Not specified",
            "R1 Research University",
            "R2 Research University",
            "Medical School / Academic Medical Center",
            "NCI / NIMH Designated Center",
            "Teaching Hospital",
            "Community College or Small University",
            "Independent Research Institute",
            "Government Lab (NIH, CDC, etc.)",
            "Industry / Private Sector"
        ],
        index=0,
        help="Affects the Environment criterion score."
    )

    study_section = st.text_input(
        "Study Section (optional)",
        placeholder="e.g. BDCN, CNS, BBBP, DP4...",
        help="Different panels weight the five criteria differently."
    )

    st.divider()

    # Stage indicator
    if STAGE2_AVAILABLE:
        st.success("⚡ Stage 2 active — dynamic retrieval enabled")
    else:
        st.info("📚 Stage 1 mode — using static corpus")

    st.divider()
    st.caption("GrantScore AI v0.3 — Prototype")
    st.caption("Confidential. Not for distribution.")

# ── Main input: Grant draft ───────────────────────────────────
st.subheader("Paste your grant abstract or specific aims")
st.caption("💡 Tip: The specific aims page gives richer feedback than the abstract alone.")

draft_text = st.text_area(
    label="Grant draft",
    placeholder="Paste your abstract or specific aims page here...",
    height=280,
    label_visibility="collapsed"
)

# ── Main input: PI experience ─────────────────────────────────
st.subheader("Describe your team's qualifications")
st.caption("Optional but strongly recommended — significantly improves Investigators criterion accuracy.")

pi_summary = st.text_area(
    label="PI experience",
    placeholder=(
        "Describe your team's relevant experience in 3-5 sentences.\n\n"
        "Include: years of experience in this area, number of relevant "
        "publications, prior NIH funding history (grant numbers if available), "
        "key collaborators, and any relevant patents or clinical expertise.\n\n"
        "Example: 'Our team has 18 years of combined experience in translational "
        "neuroscience. The PI has published 24 peer-reviewed papers on hippocampal "
        "neuroplasticity and holds one relevant patent. We have completed two prior "
        "NIH-funded studies (R21 MH112345, R01 MH123456) and have established "
        "collaborations with 3 NCI-designated cancer centers.'"
    ),
    height=160,
    label_visibility="collapsed"
)

# ── Run button ────────────────────────────────────────────────
run_button = st.button(
    "🎯 Score my grant",
    type="primary",
    disabled=not (api_key and draft_text),
    use_container_width=True
)

if not api_key:
    st.info("👈 Enter your Anthropic API key in the sidebar to get started.")


# ── Prompt builder ────────────────────────────────────────────
def build_prompt(draft, agency, mechanism, institution_type,
                 study_section, pi_summary,
                 funded_texts, unfunded_texts):

    funded_block = ""
    for i, ex in enumerate(funded_texts, 1):
        funded_block += f"\n[Funded Example {i}]\n{ex.strip()}\n"

    unfunded_block = ""
    for i, ex in enumerate(unfunded_texts, 1):
        unfunded_block += f"\n[Unfunded Example {i}]\n{ex.strip()}\n"

    institution_context = ""
    if institution_type and institution_type != "Not specified":
        institution_context = f"""
INSTITUTION TYPE: {institution_type}
Apply this when scoring the Environment criterion. R1 universities and
NCI/NIMH-designated centers typically score 1-3/9 when they demonstrate
named core facilities, existing cohorts, or established collaborations.
Teaching hospitals and smaller institutions score 4-6/9 unless they
describe specific infrastructure directly relevant to the proposed work.
Community colleges and independent institutes score 6-8/9 unless
exceptional resources are described.
"""

    study_section_context = ""
    if study_section and study_section.strip():
        study_section_context = f"""
STUDY SECTION: {study_section.strip().upper()}
Calibrate your review to the known priorities of this panel. For example:
BDCN panels scrutinize mechanistic rigor heavily. DP4 panels weight
translational feasibility and clinical applicability. CNS panels expect
strong neuroscience mechanistic framing. If the study section is not one
you recognize, apply general NIH R01 review standards.
"""

    if pi_summary and pi_summary.strip():
        pi_context = f"""
INVESTIGATOR PROFILE (provided by applicant):
{pi_summary.strip()}

Apply this when scoring the Investigators criterion. Compare against funded
corpus patterns: strong applications cite specific years of domain expertise,
publication counts with numbers, prior NIH funding by grant number, and
named collaborators or institutional partnerships. Vague language like
"our team is experienced" matches the unfunded corpus pattern and should
score 7-8/9. Specific credentials with numbers score 2-3/9.
"""
    else:
        pi_context = """
INVESTIGATOR PROFILE: Not provided by applicant.
Score the Investigators criterion based only on what appears in the draft
text itself. Note in your feedback that providing a PI summary would
significantly improve the accuracy of this criterion score.
"""

    return f"""You are a chartered {agency} peer reviewer who has served on
standing study sections for 20+ years and scored thousands of {mechanism}
applications. You apply the official {agency} review criteria rigorously
and without sentiment.

{NIH_RUBRIC}
{institution_context}{study_section_context}{pi_context}
Below are the most semantically similar examples from a labeled corpus of
real {agency} {mechanism} applications — selected specifically because they
are closest in topic and methodology to the draft being evaluated. Study
the patterns: what distinguishes funded from unfunded grants across all
five criteria?

=== FUNDED EXAMPLES (most similar to your draft, strong applications) ===
{funded_block}

=== WEAK / UNFUNDED EXAMPLES (most similar to your draft) ===
{unfunded_block}

=== DRAFT APPLICATION TO EVALUATE ===
Agency: {agency} | Mechanism: {mechanism}
{draft.strip()}

Evaluate the draft using all five NIH criteria. Be specific — reference
exact phrases from the draft and compare them directly to patterns in the
funded/unfunded corpus above. Avoid generic advice. Every weakness must
cite a specific missing element with a funded corpus example that has it.

Respond in exactly this format:

PREDICTED SCORE: [1-100 NIH-style, where 10 = exceptional/top 10%,
50 = average, 90 = poor — lower is better, matching NIH convention]
ESTIMATED PERCENTILE: [e.g. "Top 10-15%" or "Bottom 40%"]
CONFIDENCE: [Low / Medium / High] — [one sentence reason]

CRITERION SCORES (1=best, 9=worst):
- Significance: X/9
- Innovation: X/9
- Approach: X/9
- Investigators: X/9
- Environment: X/9

TOP 3 STRENGTHS:
1. [cite specific phrase from draft + compare to funded corpus pattern]
2. [cite specific phrase from draft + compare to funded corpus pattern]
3. [cite specific phrase from draft + compare to funded corpus pattern]

TOP 3 WEAKNESSES:
1. [name the missing element + quote a funded example that has it]
2. [name the missing element + quote a funded example that has it]
3. [name the missing element + quote a funded example that has it]

PRIORITY REWRITE:
Original: "[quote the weakest sentence verbatim]"
Rewritten: "[stronger version with specific data, mechanism, or credential added]"
Rationale: [one sentence explaining what the rewrite adds and why it matters]

VERDICT: [2 sentences max — lead with the biggest gap, end with potential]"""


# ── Run and display ───────────────────────────────────────────
if run_button:
    with st.spinner("Evaluating against corpus... (~10-15 seconds)"):
        try:
            # ── Stage 2: dynamic retrieval ────────────────────
            if STAGE2_AVAILABLE:
                funded_texts, unfunded_texts = retrieve_similar(
                    draft_text,
                    n_funded=5,
                    n_unfunded=3
                )
                retrieval_mode = "⚡ Stage 2 — dynamic retrieval"
            else:
                # ── Stage 1 fallback ──────────────────────────
                funded_texts   = funded_examples_text
                unfunded_texts = unfunded_examples_text
                retrieval_mode = "📚 Stage 1 — static corpus"

            # ── Score with Claude ─────────────────────────────
            client = anthropic.Anthropic(api_key=api_key)
            message = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1800,
                messages=[{
                    "role": "user",
                    "content": build_prompt(
                        draft_text,
                        agency,
                        mechanism,
                        institution_type,
                        study_section,
                        pi_summary,
                        funded_texts,
                        unfunded_texts
                    )
                }]
            )
            result = message.content[0].text
            tokens_used = message.usage.input_tokens + message.usage.output_tokens

            # ── Display report ────────────────────────────────
            st.divider()
            st.subheader("📋 Evaluation Report")
            st.caption(
                f"{retrieval_mode}  |  Agency: {agency}  |  "
                f"Mechanism: {mechanism}  |  "
                f"Institution: {institution_type}  |  "
                f"Study Section: {study_section or 'Not specified'}  |  "
                f"Tokens used: {tokens_used:,}"
            )
            st.info(
                "📊 **NIH scoring convention:** lower scores = stronger application  "
                "(10 = exceptional / top 10%,   50 = average,   90 = poor)"
            )
            st.markdown(result)
            st.divider()

            # ── Download ──────────────────────────────────────
            st.download_button(
                label="⬇️ Download report as .txt",
                data=(
                    f"GRANTSCORE AI — EVALUATION REPORT\n"
                    f"Retrieval mode: {retrieval_mode}\n"
                    f"Agency: {agency} | Mechanism: {mechanism}\n"
                    f"Institution: {institution_type}\n"
                    f"Study Section: {study_section or 'Not specified'}\n"
                    f"PI Summary: {pi_summary.strip() if pi_summary else 'Not provided'}\n"
                    f"{'='*60}\n\n{result}"
                ),
                file_name="grantscore_report.txt",
                mime="text/plain"
            )

        except anthropic.AuthenticationError:
            st.error("❌ Invalid API key. Check your key at console.anthropic.com.")
        except Exception as e:
            st.error(f"❌ Something went wrong: {str(e)}")
