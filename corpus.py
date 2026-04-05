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
# DOMAIN: Neuroscience / Mental Health / Neurological Disorders
# MECHANISM: R01
# ============================================================

# ── FUNDED EXAMPLES ─────────────────────────────────────────
# These abstracts represent successfully funded R01 applications
# exhibiting strong preliminary data, mechanistic clarity,
# investigator credentials, and explicit gap statements.

funded_examples = [
    {
        "text": """Identifying molecular drivers of Alzheimer’s disease and related dementias (AD/ADRD) pathologies is an urgent public health priority. This is especially important in persons of African Ancestry. The overall goal of the proposed study is to identify genes and proteins that drive common AD/ADRD pathologic traits. We previously used multi-level omics to identify molecular drivers of AD/ADRD pathologic traits in non-Latinx whites. The proposed study, submitted in response to NOT-AG-18-053 will extend this work by leveraging an unique, ongoing, diverse study being conducted in Sao Paulo, Brazil, called “Pathology, Alzheimer´s and Related Dementias Study” (PARDoS) and five other diverse cohorts in the USA, with whole genome sequencing (WGS) on more than 1350 diverse autopsied participants. PARDoS is prospectively generating neuropathologic and clinical AD/ADRD traits, and DNA on admixed Brazilians of European and African, and to a lesser extent Native Brazilian ancestry. The proposal has the following Aims. Aim 1 will generate WGS on an additional 7650 persons in collaboration with the Alzheimer’s Disease Sequencing Project (ADSP). Aim 2 will perform deep admixture mapping of known SNPs for Alzheimer’s dementia, to determine their associations with AD/ADRD neuropathologic phenotypes in 6500 admixed Brazilian brains followed generalization to 300 diverse brains from the USA, and discovery analyses for 5500 Brazilians followed by generalization to 2000 diverse samples in the USA. Aim 3 will computationally determine telomere length (TL) and examine their association with AD/ADRD clinical and pathologic traits. An exploratory analysis will examine for rare variant associations with AD/ADRD neuropathologic traits. Aim 5 will examine the association of mitochondrial DNA to AD/ADRD traits.""",
        "label": "funded",
        "tier": "strong",
        "institution": "Medical School / Academic Medical Center",
        "study_section": "Special Emphasis Panel[ZRG1 PSE-H (55)]",
        "fiscal_year": "2023",
        "source": "NIH Reporter R01AG075927",
        "pi": "Bennett, David A.",
        "award_amount": 3671787,
        "notes": "Multi-cohort WGS study, high-profile PI, above-average award"
    },
    {
        "text": """Over 250,000 women in the United States are living with HIV, but limited research has addressed the physical and mental health outcomes among younger women living with HIV (WLHIV). Because health status in the reproductive years and surrounding pregnancy critically affects lifelong health, understanding health outcomes among young WLHIV of reproductive age before, during, and after pregnancy is of substantial public health importance in the US and worldwide. The maternal outcomes of WLHIV are inextricably linked to the long-term health and survival of their children. The Pediatric HIV/AIDS Cohort Study (PHACS), conducted at 21 sites across the US and Puerto Rico, has been following young WLHIV of reproductive age and their children since 2007, with over 2000 birth mothers and >2800 HIV-exposed uninfected (HEU) children. Mothers with perinatally acquired HIV (PHIV) are of specific interest, and the PHACS network includes >400 such women with PHIV (WPHIV) along with their 251 HEU children. Utilizing the successful and longstanding PHACS research infrastructure and existing cohorts, we will establish the Health Outcomes around Pregnancy and Exposure to HIV/Antiretrovirals (HOPE) cohort, a cohort of 2000 pregnant, non-pregnant or nulliparous WLHIV of reproductive age from geographically diverse, high HIV prevalence areas. Leveraging PHACS, cost-effective and targeted enrollment and follow-up for longitudinal data collection will be achieved; we will also establish a rich biorepository which links WLHIV to their children’s data and biospecimens. Thus, the HOPE research platform will support high impact scientific studies central to the health of young WLHIV. Our scientific aims for the HOPE cohort are: (1) to evaluate the effects of HIV-related disease and treatment factors on reproductive health, non-communicable diseases, and oral health of WLHIV as well as psychosocial determinants of these health outcomes (engagement in care, mental health diagnoses, racism, inequity and stigma, disclosure of HIV, and substance use/misuse), and (2) To assess child health outcomes and their impact on the health of WLHIV, including maternal HIV disease progression, antiretroviral therapy (ART) adherence, engagement in care and maternal mental health. Overall, HOPE will create a platform to explore the multilevel determinants and mechanisms that influence the short and longer-term health of WLHIV during their reproductive years, as well as the health of their children, and will serve as a resource for future multidisciplinary studies in areas such as genetics and epigenetics, microbiome/virome/proteomes and immune activation, to provide better understanding of potential inflammatory and epigenetic processes associated with these outcomes.""",
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
        "text": """The goal of this project is to leverage the diverse sample in our Human Connectome Project (HCP) Study, Connectomics in Brain Aging (COBRA) , to investigate the role(s) of structural and social determinants of health in the natural history of Alzheimer’s Disease (AD) utilizing a health equity framework. We propose that racial inequities in the development of cognitive impairments in the context of AD are driven by pervasive structural and institutionalized inequities that shape risk and disadvantage at multiple levels, including biological, environmental, behavioral, sociocultural, as proposed in the NIA Health Disparities Research Framework. Our organizing principle is that the expression of cognitive dysfunction in the elderly is the result of two independent processes affecting the connectome — the first is the neuropathology associated with AD. The second process historically has been referred to as “modifiable individual risk factors”, however, this fails to recognize that individual risk is influenced by factors that are outside of an individual’s control, and which will be measured using a health equity framework. We will augment our existing sample (50% Black, 65% Female) with an additional 150 participant (total sample ~400 with up to four study visits). Each of the participants will contribute the HCP-specified demographic, behavioral and laboratory data. All of the participants will undergo extensive brain imaging biannually including MRI and PET (amyloid and tau tracers). All of the MRI data will be uploaded to the Connectome Coordinating Facility, and the behavioral/cognitive, PET data will be uploaded to the NIMH Data Archive. Locally, we will use these data to address specific questions related to structure, function, AD, aging and vascular disease in multi-modality studies leveraging the differential advantages of MRI, fMRI, and in vivo Aβ and tau imaging.""",
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
     {
        "text": """Dementia with Lewy bodies (DLB) is the second most common cause of neurodegenerative dementia after Alzheimer’s disease (AD). DLB is a more rapidly progressive disease than AD, with a median time from diagnosis to death or nursing home admission that is half that seen in AD and is associated with extensive burden on both patients and family caregivers. There is a great unmet medical need, with no approved treatments, only AD and Parkinson’s disease (PD) drugs used off-label to partially or temporarily relieve some of its severe cognitive and motor symptoms. The proposed treatment, neflamapimod, an orally bioavailable, highly specific inhibitor of the intracellular enzyme p38 mitogen activated protein kinase alpha (p38α), is in clinical development by EIP Pharma with a phase 2a study in DLB and phase 2 studies in early AD already completed. Preclinical data indicate that neflamapimod, through inhibiting p38α, therapeutically targets specific pathogenic mechanisms underlying dysfunction and degeneration of neurons in a part of the brain called the basal forebrain, abnormalities in which are considered to be the major pathogenic drivers of the dementia in DLB. For example, neflamapimod increased the number of functioning basal forebrain cholinergic neurons in Ts2 transgenic mice that, along with modeling Down syndrome, develop neurodegeneration in the basal forebrain cholinergic system. Together, such evidence provides a strong scientific rationale for neflamapimod as a disease modifying treatment for DLB. In accordance with this, neflamapimod received Fast-Track designation by the FDA for DLB. A recently completed phase 2a exploratory (i.e., hypothesis-generating) clinical trial (NCT04001517) in 91 patients with mild-to-moderate DLB, also receiving cholinesterase inhibitor therapy, provided preliminary evidence of clinical efficacy of neflamapimod on various cognitive, motor, and functional aspects of the disease. The proposed phase 2b trial will confirm and expand upon these results. The Specific Aims are to, in the context of performing a phase 2b randomized, double- blind, placebo-controlled, 16-week treatment study of neflamapimod (40mg TID) in 160 subjects with mild-to-moderate DLB: (Aim 1). Demonstrate that neflamapimod improves cognition and function, based on primary (Neuropsychological Test Battery) and secondary (Clinical Dementia Rating Scale sum of boxes, Timed Up and Go test, The Alzheimer’s Disease Cooperative Study – Clinical Global Impression of Change) efficacy measures in patients with mild-to-moderate DLB receiving cholinesterase inhibitors; (Aim 2). Assess neuropsychiatric outcomes and safety/tolerability during treatment with neflamapimod in patients with DLB; and (Aim 3). Assess effects of neflamapimod on electroencephalographic (EEG) measures of DLB, specifically beta functional connectivity and alpha-reactivity; both markers of basal forebrain cholinergic dysfunction. Successful completion of this phase 2b trial will inform our pivotal phase 3 trial, advancing neflamapimod as a disease- modifying treatment for DLB and providing hope for these patients and their families.""",
        "label": "funded",
        "tier": "strong",
        "institution": "R1 Research University",
        "study_section": "Adult Psychopathology and Disorders of Aging Study Section[APDA]",
        "fiscal_year": "2023",
        "source": "NIH Reporter R01AG080536-01",
        "pi": "ALAM, JOHN",
        "award_amount": 6682055,
        "notes": "On-domain neuroscience, dementia, Alzheimer’s disease, phase 2b trial, RCT"
    },
      {
        "text": """Novel approaches to reduce the risk of cognitive decline and Alzheimer's disease and related dementias (ADRD) in older adults are urgently needed given the aging of the population. Over the past decade, observational research has implicated peripheral hearing loss as being one of the largest potentially modifiable risk factors for dementia that may account for 8-9% of all dementia cases. Hypothesized pathways underlying this observed association may be modifiable with hearing loss treatment consisting of the use of hearing technologies (e.g., hearing aids) and rehabilitative training. The Aging & Cognitive Health Evaluation in Elders (ACHIEVE) study is an ongoing, NIA-sponsored Phase III RCT (R01AG055426, MPIs: Lin/Coresh) investigating whether hearing loss treatment versus an aging education control intervention reduces cognitive decline over a three-year follow- up period. From 2018-19, we recruited 977 adults ages 70-84 with untreated mild-to-moderate hearing loss who were randomized 1:1 at baseline (Year 0) to receive hearing intervention (HI; best-practice hearing services and technologies) versus a successful aging (SA) education control intervention (i.e., one-on-one sessions with a health educator covering topics important for healthy aging). Participants are currently being followed semiannually at the ACHIEVE field sites with final Year 3 study visits scheduled from 2021-22. After their Year 3 visit, all participants randomized to the SA education control group will also be offered the hearing intervention. Final Year 3 results from this original trial will indicate whether hearing intervention (versus a successful aging control intervention) reduces cognitive decline over a 3-year interval after randomization. We now propose to continue following the ACHIEVE cohort for an additional 3 years (i.e., up to Year 6) to determine the long- term effects of hearing intervention (i.e., participants randomized to HI at Year 0) versus successful aging/delayed HI control (i.e., participants randomized to SA at Year 0 and offered HI after their Year 3 visit) on cognitive and brain outcomes. Given that cognitive impairment typically reflects the slow accumulation of pathologic changes, the benefits of HI in slowing this decline may not be fully appreciable within just 3 years. Therefore, this 6-year follow-up of the cohort will allow us to fully evaluate the longer, cumulative impact of HI on older adults. Such findings will complement the main trial results in 2023 and directly inform clinical and policy decisions around the potential use of hearing interventions to reduce the risk of ADRD. This proposed study has the following aims: Aim 1 To determine the long-term effect of HI versus SA/Delayed HI control on rates of the co-primary outcomes of: (a) cognitive decline and (b) incident mild cognitive impairment (MCI)/dementia. Aim 2 To determine the long-term effect of HI versus SA/Delayed HI control on changes in brain MRI measures of: (a) regional brain volumes and (b) white matter tract integrity. Secondary Aims: 1) To investigate potential factors contributing to HI treatment effect heterogeneity; 2) To investigate health care expenditures and utilization between the HI vs SA/Delayed HI control groups by analyzing Medicare claims data.""",
        "label": "funded",
        "tier": "strong",
        "institution": "R1 Research University",
        "study_section": "Special Emphasis Panel[ZRG1 BBBP-H (55)]",
        "fiscal_year": "2022",
        "source": "NIH Reporter R01AG076518-01",
        "pi": "LIN, FRANK R",
        "award_amount": 4123874,
        "notes": "On-domain neuroscience, cognitive decline, Alzheimer’s disease, hearing intervention, RCT"
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
