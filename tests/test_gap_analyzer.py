from tools.resume_parser import read_resume
from agents.resume_agent import analyze_resume
from agents.gap_analyzer import gap_analyzer
from tools.hybrid_retriever import hybrid_retriever

resume = read_resume("data/sample_resume.txt")

resume_analysis = analyze_resume(resume)

company_context = "\n".join(
    hybrid_retriever("amazon interview requirements")
)

result = gap_analyzer(
    resume_analysis,
    company_context
)

print(result)