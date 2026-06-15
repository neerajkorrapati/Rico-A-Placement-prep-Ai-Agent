from agents.personalised_roadmap_agent import road_map_agent
from tools.resume_parser import read_resume

from agents.resume_agent import analyze_resume

from agents.gap_analyzer import gap_analyzer
from tools.hybrid_retriever import hybrid_retriever

resume = read_resume(
    "data/sample_resume.txt"
)

resume_analysis = analyze_resume(
    resume
)

company_context = "\n".join(
    hybrid_retriever(
        "Amazon interview requirements"
    )
)

gap_result = gap_analyzer(
    company_context,
    resume_analysis
)

roadmap = road_map_agent(
    gap_result
)

print("\n=== PERSONALIZED ROADMAP ===\n")

print(roadmap)