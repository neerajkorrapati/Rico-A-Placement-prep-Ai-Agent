from tools.retriever import retrieve_context

def research_agent(query):
    context = retrieve_context(query)

    return context