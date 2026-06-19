from typing import TypedDict
from agents.resume_agent import resume_agent
from agents.gap_analyzer import gap_analyzer
from tools.hybrid_retriever import hybrid_retriever
from agents.roadmap_agent import roadmap_agent
from langgraph.graph import (START,StateGraph,END)

#State Definitions:
class PlacementState(TypedDict):
    resume_text:str
    company:str
    company_context:str
    resume_analysis:dict
    gap_analysis:dict
    roadmap:dict
#node definitions
def resume_node(state: PlacementState):
    result=resume_agent(state["resume_text"])
    return { "resume_analysis":result }
def gap_node(state: PlacementState):
    company_context="\n".join(hybrid_retriever(f"{state['company']} interview requirements"))

    result=gap_analyzer(company_context,state["resume_analysis"])
    return { "gap_analysis":result}
def roadmap_node(state:PlacementState):
    result=roadmap_agent(state["gap_analysis"])
    return {"roadmap":result}   


graph=StateGraph(PlacementState)
graph.add_node("resume_node",resume_node)
graph.add_node("gap_node",gap_node)
graph.add_node("roadmap_node",roadmap_node)

graph.add_edge(START,"resume_node")
graph.add_edge("resume_node","gap_node")
graph.add_edge("gap_node","roadmap_node")
graph.add_edge("roadmap_node",END)

workflow=graph.compile()
#result=workflow.invoke()


