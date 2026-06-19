from typing import TypedDict    
from langgraph.graph import(
    StateGraph,START,END
)
class State(TypedDict):
    number:int

def add_two(state:State):
    return{
        "number":state["number"]+2
    }
graph =StateGraph(State)
graph.add_node("add_two",add_two)

graph.add_edge(START,"add_two")
graph.add_edge("add_two",END)
workflow=graph.compile()

result=workflow.invoke(
    {
        "number":5
    }
)

print(result)