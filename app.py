import streamlit as st
import chromadb
from tools.resume_parser import read_resume
def initialize_database():

    client = chromadb.PersistentClient(
        path="data/chromadb"
    )

    collection = client.get_or_create_collection(
        name="company_knowledge"
    )

    if collection.count() == 0:

        import ingest_documents

initialize_database()
from agents.placement_graph import workflow
# Page Config

st.set_page_config(
    page_title="Placement Prep AI",
    page_icon="🚀",
    layout="wide"
)
# Custom Styling

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0;
}

.sub-title {
    color: #888;
    margin-bottom: 2rem;
}

.section-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

.card {
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #262730;
    background-color: #111111;
}

.skill-pill {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    margin: 0.2rem;
    border-radius: 20px;
    background: #1f2937;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Header

st.markdown(
    '<div class="main-title">Placement Prep AI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">Career Intelligence Dashboard</div>',
    unsafe_allow_html=True
)
# Sidebar

with st.sidebar:

    st.header("Candidate Setup")
    #here
    AVAILABLE_COMPANIES = [
    "Amazon",
    "Google",
    "Microsoft",
    "Goldman Sachs",
    "Walmart",
    "Adobe",
    "Uber",
    "Atlassian"
]

    company = st.selectbox(
        "Target Company",
        AVAILABLE_COMPANIES
    )
    uploaded_file = st.file_uploader(
        "Upload Resume (.txt)",
        type=["txt"]
    )
    generate = st.button(
        "Generate Analysis",
        use_container_width=True
    )
# Workflow

if uploaded_file and generate:

    with open("temp_resume.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = read_resume(
        "temp_resume.txt"
    )

    with st.spinner("Generating Career Intelligence Report..."):

        result = workflow.invoke(
            {
                "resume_text": resume_text,
                "company": company
            }
        )

    report = result["final_report"]

    resume_analysis = report["resume_analysis"]
    gap_analysis = report["gap_analysis"]
    roadmap = report["roadmap"]
    interview_questions = report["interview_questions"]
    company_research = report["company_research"]

    ats = report.get("ats_analysis")
    # Metrics
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        if ats:
            st.metric(
                "ATS Score",
                ats["ats_score"]
            )
        else:
            st.metric(
                "ATS Score",
                "N/A"
            )
    with col2:
        if ats:
            st.metric(
                "Keyword Match",
                f"{ats['keyword_match']}%"
            )
        else:
            st.metric(
                "Keyword Match",
                "N/A"
            )
    with col3:
        st.metric(
            "Target Company",
            company
        )
    # --------------------------------------------------
    # Resume Analysis
    # --------------------------------------------------

    st.divider()

    st.subheader("Candidate Profile")

    left, right = st.columns(2)

    with left:

        st.markdown("### Strengths")

        for item in resume_analysis["strengths"]:
            st.markdown(f"✓ {item}")

        st.markdown("### Technical Skills")

        for skill in resume_analysis["technical_skills"]:
            st.markdown(
                f"<span class='skill-pill'>{skill}</span>",
                unsafe_allow_html=True
            )

    with right:

        st.markdown("### Weaknesses")

        for item in resume_analysis["weaknesses"]:
            st.markdown(f"• {item}")

        st.markdown("### Improvements")

        for item in resume_analysis["improvements"]:
            st.markdown(f"• {item}")

    # Gap Analysis
    st.divider()
    st.subheader("Skill Gap Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Covered Skills")

        for skill in gap_analysis["covered_skills"]:
            st.markdown(f"✓ {skill}")

    with col2:

        st.markdown("### Missing Skills")

        for skill in gap_analysis["missing_skills"]:
            st.markdown(f"⚠️ {skill}")

    st.markdown("### Recommendations")

    for rec in gap_analysis["recommendations"]:
        st.markdown(f"• {rec}")
    # Roadmap
    st.divider()
    st.subheader("4 Week Preparation Plan")
    for week, tasks in roadmap.items():

        with st.expander(
            week.replace("_", " ").title(),
            expanded=False
        ):

            for task in tasks:
                st.markdown(f"• {task}")

    # --------------------------------------------------
    # Interview Questions
    # --------------------------------------------------

    st.divider()

    st.subheader("Interview Preparation")

    for category, questions in interview_questions.items():

        st.markdown(
            f"### {category.replace('_',' ').title()}"
        )

        for question in questions:
            st.markdown(f"• {question}")
    # Company Research
    st.divider()
    st.subheader("Company Intelligence")
    st.markdown("### Overview")
    st.write(
        company_research["company_overview"]
    )
    col1, col2 = st.columns(2)
    with col1:

        st.markdown("### Tech Stack")

        for tech in company_research["tech_stack"]:
            st.markdown(f"• {tech}")

    with col2:
        st.markdown("### Interview Focus")
        for topic in company_research["interview_focus"]:
            st.markdown(f"• {topic}")
    if "important_topics" in company_research:

        st.markdown("### Important Topics")

        for topic in company_research["important_topics"]:
            st.markdown(f"• {topic}")

else:

    st.info(
        "Upload a resume and click 'Generate Analysis' to begin."
    )