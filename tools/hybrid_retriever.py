from tools.keyword_search import keyword_search
from tools.retriever import retrieve_context
#combines the search results from both keyword and semantic , eliminates duplicate results, and returns a improved search result.
def hybrid_retriever(query):
    keyword_results= keyword_search(query)
    semantic_results=retrieve_context(query)
    combined=[]
    if(keyword_results):
        combined+=keyword_results
    if(semantic_results):
        combined+=semantic_results
    combined=list(dict.fromkeys(combined))

    return combined
