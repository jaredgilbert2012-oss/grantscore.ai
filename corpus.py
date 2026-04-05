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

funded_examples = [
    {
        "text": """ABSTRACT Identifying molecular drivers of Alzheimer’s disease and related dementias (AD/ADRD) pathologies is an urgent public health priority. This is especially important in persons of African Ancestry. The overall goal of the proposed study is to identify genes and proteins that drive common AD/ADRD pathologic traits. We previously used multi-level omics to identify molecular drivers of AD/ADRD pathologic traits in non-Latinx whites. The proposed study, submitted in response to NOT-AG-18-053 will extend this work by leveraging an unique, ongoing, diverse study being conducted in Sao Paulo, Brazil, called “Pathology, Alzheimer´s and Related Dementias Study” (PARDoS) and five other diverse cohorts in the USA, with whole genome sequencing (WGS) on more than 1350 diverse autopsied participants. PARDoS is prospectively generating neuropathologic and clinical AD/ADRD traits, and DNA on admixed Brazilians of European and African, and to a lesser extent Native Brazilian ancestry. The proposal has the following Aims. Aim 1 will generate WGS on an additional 7650 persons in collaboration with the Alzheimer’s Disease Sequencing Project (ADSP). Aim 2 will perform deep admixture mapping of known SNPs for Alzheimer’s dementia, to determine their associations with AD/ADRD neuropathologic phenotypes in 6500 admixed Brazilian brains followed generalization to 300 diverse brains from the USA, and discovery analyses for 5500 Brazilians followed by generalization to 2000 diverse samples in the USA. Aim 3 will computationally determine telomere length (TL) and examine their association with AD/ADRD clinical and pathologic traits. An exploratory analysis will examine for rare variant associations with AD/ADRD neuropathologic traits. Aim 5 will examine the association of mitochondrial DNA to AD/ADRD traits.""",
        "label": "funded",
        "tier": "strong",
        "institution": "Medical School / Academic Medical Center",
        "study_section": "Special Emphasis Panel[ZRG1 PSE-H (55)]",  # fill in if you find it
        "fiscal_year": "2023",
        "source": "NIH Reporter R01AG075927",
        "pi": "Bennett, David A.",
        "award_amount": 3671787,
        "notes": "Multi-cohort WGS study, high-profile PI, above-average award"
    },
    {
        "text": """Abstract Over 250,000 women in the United States are living with HIV, but limited research has addressed the physical and mental health outcomes among younger women living with HIV (WLHIV). Because health status in the reproductive years and surrounding pregnancy critically affects lifelong health, understanding health outcomes among young WLHIV of reproductive age before, during, and after pregnancy is of substantial public health importance in the US and worldwide. The maternal outcomes of WLHIV are inextricably linked to the long-term health and survival of their children. The Pediatric HIV/AIDS Cohort Study (PHACS), conducted at 21 sites across the US and Puerto Rico, has been following young WLHIV of reproductive age and their children since 2007, with over 2000 birth mothers and >2800 HIV-exposed uninfected (HEU) children. Mothers with perinatally acquired HIV (PHIV) are of specific interest, and the PHACS network includes >400 such women with PHIV (WPHIV) along with their 251 HEU children. Utilizing the successful and longstanding PHACS research infrastructure and existing cohorts, we will establish the Health Outcomes around Pregnancy and Exposure to HIV/Antiretrovirals (HOPE) cohort, a cohort of 2000 pregnant, non-pregnant or nulliparous WLHIV of reproductive age from geographically diverse, high HIV prevalence areas. Leveraging PHACS, cost-effective and targeted enrollment and follow-up for longitudinal data collection will be achieved; we will also establish a rich biorepository which links WLHIV to their children’s data and biospecimens. Thus, the HOPE research platform will support high impact scientific studies central to the health of young WLHIV. Our scientific aims for the HOPE cohort are: (1) to evaluate the effects of HIV-related disease and treatment factors on reproductive health, non-communicable diseases, and oral health of WLHIV as well as psychosocial determinants of these health outcomes (engagement in care, mental health diagnoses, racism, inequity and stigma, disclosure of HIV, and substance use/misuse), and (2) To assess child health outcomes and their impact on the health of WLHIV, including maternal HIV disease progression, antiretroviral therapy (ART) adherence, engagement in care and maternal mental health. Overall, HOPE will create a platform to explore the multilevel determinants and mechanisms that influence the short and longer-term health of WLHIV during their reproductive years, as well as the health of their children, and will serve as a resource for future multidisciplinary studies in areas such as genetics and epigenetics, microbiome/virome/proteomes and immune activation, to provide better understanding of potential inflammatory and epigenetic processes associated with these outcomes.""",
        "label": "funded",
        "tier": "strong",
        "institution": "R1 Research University",
        "study_section": "Special Emphasis Panel[ZHD1 DSR-A (50)]",
        "fiscal_year": "2020",
        "source": "NIH Reporter R01HD101351",
        "pi": "Williams, Paige L. et al.",
        "award_amount": 3000000,
        "notes": "Multi-PI Harvard cohort, adjacent domain (HIV/women's health)"
    },
    {
        "text": """Abstract The goal of this project is to leverage the diverse sample in our Human Connectome Project (HCP) Study, Connectomics in Brain Aging (COBRA) , to investigate the role(s) of structural and social determinants of health in the natural history of Alzheimer’s Disease (AD) utilizing a health equity framework. We propose that racial inequities in the development of cognitive impairments in the context of AD are driven by pervasive structural and institutionalized inequities that shape risk and disadvantage at multiple levels, including biological, environmental, behavioral, sociocultural, as proposed in the NIA Health Disparities Research Framework. Our organizing principle is that the expression of cognitive dysfunction in the elderly is the result of two independent processes affecting the connectome — the first is the neuropathology associated with AD. The second process historically has been referred to as “modifiable individual risk factors”, however, this fails to recognize that individual risk is influenced by factors that are outside of an individual’s control, and which will be measured using a health equity framework. We will augment our existing sample (50% Black, 65% Female) with an additional 150 participant (total sample ~400 with up to four study visits). Each of the participants will contribute the HCP-specified demographic, behavioral and laboratory data. All of the participants will undergo extensive brain imaging biannually including MRI and PET (amyloid and tau tracers). All of the MRI data will be uploaded to the Connectome Coordinating Facility, and the behavioral/cognitive, PET data will be uploaded to the NIMH Data Archive. Locally, we will use these data to address specific questions related to structure, function, AD, aging and vascular disease in multi-modality studies leveraging the differential advantages of MRI, fMRI, and in vivo Aβ and tau imaging.""",
        "label": "funded",
        "tier": "strong",
        "institution": "R1 Research University",
        "study_section": "Special Emphasis Panel[ZRG1 BDCN-F (55)]",
        "fiscal_year": "2022",
        "source": "NIH Reporter R01AG072641",
        "pi": "Cohen, Ann D.",
        "award_amount": 2416844,
        "notes": "On-domain neuroscience, health disparities framework, Pitt"
    },
]
# ── UNFUNDED / WEAK EXAMPLES ─────────────────────────────────
# These abstracts represent applications that were not funded
# or scored poorly. Use anonymized real examples where possible,
# or well-constructed weak examples that illustrate common gaps.

unfunded_examples = [
    {
        "text": """
    Mental health is increasingly recognized as important. This project
    will investigate stress in college students using surveys and interviews.
    Students will complete questionnaires about their stress levels and we
    will analyze the results. We hope to find out what causes stress and
    what might help. The findings will be useful for universities trying
    to support student wellbeing.
        """,
        "label": "unfunded",
        "tier": "weak",
        "institution": "unknown",
        "study_section": "unknown",
        "fiscal_year": "constructed",
        "source": "constructed",
        "pi": "unknown",
        "award_amount": 0,
        "notes": "Weak example — vague significance, no preliminary data"
    },
    {
        "text": """
    Depression affects many people and is a serious problem. We want to
    understand what causes depression and how we can help people who suffer
    from it. We will recruit patients from local clinics and give them
    questionnaires. Our team is interested in this area and has been
    working on mental health topics for several years. We believe this
    research will be significant and publishable.
        """,
        "label": "unfunded",
        "tier": "weak",
        "institution": "unknown",
        "study_section": "unknown",
        "fiscal_year": "constructed",
        "source": "constructed",
        "pi": "unknown",
        "award_amount": 0,
        "notes": "Weak example — no mechanistic rationale, no credentials"
    },
    {
        "text": """
    Anxiety disorders are common in the United States. This study will
    examine whether therapy helps people with anxiety feel better. We will
    compare two groups of patients over six months and measure their
    anxiety levels before and after treatment. Results will contribute to
    the literature on anxiety treatment and inform clinical practice.
        """,
        "label": "unfunded",
        "tier": "weak",
        "institution": "unknown",
        "study_section": "unknown",
        "fiscal_year": "constructed",
        "source": "constructed",
        "pi": "unknown",
        "award_amount": 0,
        "notes": "Weak example — generic methods, no gap statement"
    },
    {
        "text": """
    Building on extensive prior research demonstrating the relationship
    between stress and depression, we will conduct a randomized controlled
    trial testing cognitive behavioral therapy versus medication management
    in adults with moderate depression. We will recruit 120 participants
    from outpatient clinics and assess outcomes at 3, 6, and 12 months
    using validated instruments including the PHQ-9 and HAM-D. Our team
    has conducted prior studies in this area. Results will inform clinical
    practice guidelines for depression treatment selection.
        """,
        "label": "unfunded",
        "tier": "weak",
        "institution": "unknown",
        "study_section": "unknown",
        "fiscal_year": "constructed",
        "source": "constructed",
        "pi": "unknown",
        "award_amount": 0,
        "notes": "Weak example — technically competent but completely incremental"
    },
]

# ── Flat text lists for Stage 1 prompt ───────────────────────
# Stage 2 will use the full dicts directly for Pinecone metadata
funded_examples_text   = [entry["text"] for entry in funded_examples]
unfunded_examples_text = [entry["text"] for entry in unfunded_examples]
