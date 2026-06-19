from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)
def add2(x):
    return x+2
runnable =RunnableLambda(add2)
print(runnable.invoke(5))
chain=RunnablePassthrough()
print(chain.invoke(
    {
        "name":"neeraj k"
    }
)
)

parrallel=RunnableParallel(
    double=RunnableLambda(lambda x:x*2),
    square=RunnableLambda(lambda x:x*x)
)
print(parrallel.invoke(7))