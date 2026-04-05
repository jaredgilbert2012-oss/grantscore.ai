"""
GrantScore AI — Simple Web UI
Built with Streamlit

To run locally:
    pip install streamlit anthropic
    streamlit run grantscore_app.py

To share:
    Deploy free at share.streamlit.io
    (connect your GitHub repo, one click deploy)
"""

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

# ── Corpus (managed in corpus.py) ────────────────────────────
from corpus import funded_examples_text, unfunded_examples_text

NIH_RUBRIC = """
SCORING FRAMEWORK — NIH Peer Review Criteria
Reviewers evaluate five criteria, each scored 1 (exceptional) to 9 (poor):

1. SIGNIFICANCE — Does this address an important problem or critical barrier?
2. INNOVATION — Does it challenge existing paradigms or develop new methodologies?
3. APPROACH — Are the design, methods, and analyses rigorous and feasible?
4. INVESTIGATORS — Are the PIs well-suited to this project?
5. ENVIRONMENT — Does the institutional setting support success?
"""

# ── Sidebar: settings ────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        help="Get yours at console.anthropic.com"
    )
    agency = st.selectbox(
        "Funding Agency",
        ["NIH", "NSF", "Foundation / Private"],
        index=0
    )
    mechanism = st.selectbox(
        "Grant Mechanism",
        ["R01", "R21", "R03", "K-Award", "CAREER", "General"],
        index=0
    )
    st.divider()
    st.caption("GrantScore AI v0.1 — Prototype")
    st.caption("Confidential. Not for distribution.")

# ── Main input ───────────────────────────────────────────────
st.subheader("Paste your grant abstract or specific aims")

draft_text = st.text_area(
    label="Grant draft",
    placeholder="Paste your abstract or specific aims page here...",
    height=280,
    label_visibility="collapsed"
)

run_button = st.button(
    "🎯 Score my grant",
    type="primary",
    disabled=not (api_key and draft_text),
    use_container_width=True
)

if not api_key:
    st.info("👈 Enter your Anthropic API key in the sidebar to get started.")

# ── Scoring logic ─────────────────────────────────────────────
def build_prompt(draft, agency, mechanism):
    funded_block = ""
    for i, ex in enumerate(funded_examples_text, 1):
    funded_block += f"\n[Funded Example {i}]\n{ex.strip()}\n"

    unfunded_block = ""
    for i, ex in enumerate(unfunded_examples_text, 1):
    unfunded_block += f"\n[Unfunded Example {i}]\n{ex.strip()}\n"

    return f"""You are a chartered {agency} peer reviewer who has served on standing study sections
for 20+ years and scored thousands of {mechanism} applications.

{NIH_RUBRIC}

=== FUNDED EXAMPLES ===
{funded_block}

=== UNFUNDED EXAMPLES ===
{unfunded_block}

=== DRAFT TO EVALUATE ===
Agency: {agency} | Mechanism: {mechanism}
{draft.strip()}

Evaluate using the five criteria. Respond in exactly this format:

PREDICTED SCORE: [0–100]
ESTIMATED PERCENTILE: [e.g. "Top 10–15%"]
CONFIDENCE: [Low/Medium/High] — [one sentence reason]

CRITERION SCORES (1=best, 9=worst):
- Significance: X/9
- Innovation: X/9
- Approach: X/9
- Investigators: X/9
- Environment: X/9

TOP 3 STRENGTHS:
1. [specific phrase from draft + funded corpus comparison]
2. [specific phrase from draft + funded corpus comparison]
3. [specific phrase from draft + funded corpus comparison]

TOP 3 WEAKNESSES:
1. [missing element + quote funded example that has it]
2. [missing element + quote funded example that has it]
3. [missing element + quote funded example that has it]

PRIORITY REWRITE:
Original: "[weakest sentence verbatim]"
Rewritten: "[stronger version]"
Rationale: [one sentence]

VERDICT: [2 sentences — lead with biggest gap, end with potential]"""


# ── Run and display ───────────────────────────────────────────
if run_button:
    with st.spinner("Evaluating against corpus... (~5–10 seconds)"):
        try:
            client = anthropic.Anthropic(api_key=api_key)
            message = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1800,
                messages=[{
                    "role": "user",
                    "content": build_prompt(draft_text, agency, mechanism)
                }]
            )
            result = message.content[0].text
            tokens_used = message.usage.input_tokens + message.usage.output_tokens

            st.divider()
            st.subheader("📋 Evaluation Report")
            st.caption(f"Agency: {agency}  |  Mechanism: {mechanism}  |  Tokens used: {tokens_used:,}")
            st.markdown(result)
            st.divider()

            # Download button
            st.download_button(
                label="⬇️ Download report as .txt",
                data=f"GRANTSCORE AI — EVALUATION REPORT\n"
                     f"Agency: {agency} | Mechanism: {mechanism}\n"
                     f"{'='*60}\n\n{result}",
                file_name="grantscore_report.txt",
                mime="text/plain"
            )

        except anthropic.AuthenticationError:
            st.error("❌ Invalid API key. Check your key at console.anthropic.com.")
        except Exception as e:
            st.error(f"❌ Something went wrong: {str(e)}")
