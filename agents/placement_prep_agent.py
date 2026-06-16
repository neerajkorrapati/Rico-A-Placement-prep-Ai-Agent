from tools.resume_parser import read_resume
from tools.hybrid_retriever import hybrid_retriever
from agents.gap_analyzer import gap_analyzer
from agents.resume_agent import analyze_resume
from agents.roadmap_agent import roadmap_agent
#here we need all of the above agents to work together:
def placement_prep_agent(resume_path,target_company):
    resume_text=read_resume(resume_path)
    resume_analysis=analyze_resume(resume_text)
    company_context="\n".join(hybrid_retriever(f"{target_company} Interview requirements"))
    gap_analysis=gap_analyzer(company_context,resume_analysis)
    roadmap=roadmap_agent(gap_analysis)

    return{
        "resume_analysis":resume_analysis,
        "gap_analysis":gap_analysis,
        "roadmap":roadmap
    }
