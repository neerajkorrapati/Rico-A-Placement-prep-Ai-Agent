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

def mul_3(state:State):
    return{
        "number":state["number"]*3
    }

graph =StateGraph(State)

graph.add_node("add_two",add_two)

graph.add_node("mul_3",mul_3)


graph.add_edge(START,"add_two")
graph.add_edge("add_two","mul_3")
graph.add_edge("mul_3",END)

workflow=graph.compile()

result=workflow.invoke(
    {
        "number":5
    }
)

print(result)
