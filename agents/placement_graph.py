from typing import TypedDict,List
from agents.resume_agent import resume_agent
from agents.gap_analyzer import gap_analyzer
from agents.interview_agent import interview_agent
from tools.hybrid_retriever import hybrid_retriever
from agents.roadmap_agent import roadmap_agent
from agents.company_research_agent import company_research_agent
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
graph=StateGraph(PlacementState)
graph.add_node("resume_node",resume_node)
graph.add_node("gap_node",gap_node)
graph.add_node("roadmap_node",roadmap_node)
graph.add_node("interview_node",interview_node)
graph.add_node("company_research_node",company_research_node)

graph.add_edge(START,"resume_node")
graph.add_edge("resume_node","gap_node")
graph.add_edge("gap_node","roadmap_node")
graph.add_edge("gap_node","interview_node")
graph.add_edge("gap_node","company_research_node")
graph.add_edge("roadmap_node",END)
graph.add_edge("interview_node",END)
graph.add_edge("company_research_node",END)

workflow=graph.compile()
#result=workflow.invoke()


