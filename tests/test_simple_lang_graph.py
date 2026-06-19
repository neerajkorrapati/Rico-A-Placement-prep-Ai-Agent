from typing import TypedDict
from langgraph.graph import(
    START,END,StateGraph
)
class State(TypedDict):
    resume_text:str
    resume_analysis:str

def resume_node(state:State):
    return{
        "resume_analysis":"Python, AI ,java"
    }
graph =StateGraph(State)
graph.add_node("resume_node",resume_node)
graph.add_edge(START,"resume_node")
graph.add_edge("resume_node",END)

workflow=graph.compile()
result=workflow.invoke(
    {
    "resume_text":"My resume"
    }
)
print(result)