from tools.retriever import retrieve_context

def research_agent(query):
    context = retriever_context(query)

    return context