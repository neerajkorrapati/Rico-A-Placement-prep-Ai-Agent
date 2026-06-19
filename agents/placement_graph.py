from typing import TypedDict,List
from agents.resume_agent import resume_agent
from agents.gap_analyzer import gap_analyzer
from agents.interview_agent import interview_agent
from tools.hybrid_retriever import hybrid_retriever
from agents.roadmap_agent import roadmap_agent
from agents.company_research_agent import company_research_agent
from agents.ats_agent import ats_agent
from langgraph.graph import (START,StateGraph,END)


#State Definitions:
class PlacementState(TypedDict):
    resume_text:str
    company:str
    company_context:str
    resume_analysis:dict
    gap_analysis:dict
    roadmap:dict
    interview_questions:dict
    company_research:dict
    final_report:dict
    ats_analysis:dict
#node definitions
def resume_node(state: PlacementState):
    result=resume_agent(state["resume_text"])
    return { "resume_analysis":result }
def gap_node(state: PlacementState):
    company_context="\n".join(hybrid_retriever(f"{state['company']} interview requirements"))

    result=gap_analyzer(company_context,state["resume_analysis"])
    return { "company_context":company_context,
             "gap_analysis":result
             }
def roadmap_node(state:PlacementState):
    result=roadmap_agent(state["gap_analysis"])
    return {"roadmap":result}   
#adding new node0>to gap node
def interview_node(state:PlacementState):
    #have a dummmy test case date initially:
    result=interview_agent(state["gap_analysis"],state["company"])
    return{
        "interview_questions":result
    }

def company_research_node(state:PlacementState):
    result= company_research_agent(state["company"])
    return {
        "company_research":result
    }
def ats_node(state:PlacementState):
    result=ats_agent(state["resume_analysis"],state["gap_analysis"])
    return {"ats_analysis":result}
#creating our final -> coordinator node;
def final_report_node(state:PlacementState):
    return {
        "final_report":
        {
            "company":
            state["company"],

            "resume_analysis":
            state["resume_analysis"],

            "gap_analysis":
            state["gap_analysis"],

            "roadmap":
            state["roadmap"],

            "interview_questions":
            state["interview_questions"],

            "company_research":
            state["company_research"],

            "ats_analysis":
            state["ats_analysis"]
        }
    }

graph=StateGraph(PlacementState)
graph.add_node("resume_node",resume_node)
graph.add_node("gap_node",gap_node)
graph.add_node("roadmap_node",roadmap_node)
graph.add_node("interview_node",interview_node)
graph.add_node("company_research_node",company_research_node)
graph.add_node("ats_node",ats_node)
#adding our final report node:
graph.add_node("final_report_node",final_report_node)
    
graph.add_edge(START,"resume_node")
graph.add_edge("resume_node","gap_node")
graph.add_edge("gap_node","roadmap_node")
graph.add_edge("gap_node","interview_node")
graph.add_edge("gap_node","company_research_node")
graph.add_edge("gap_node","ats_node")
graph.add_edge("roadmap_node","final_report_node")
graph.add_edge("interview_node","final_report_node")
graph.add_edge("company_research_node","final_report_node")
graph.add_edge("ats_node","final_report_node")
graph.add_edge("final_report_node",END)

workflow=graph.compile()
#result=workflow.invoke()


