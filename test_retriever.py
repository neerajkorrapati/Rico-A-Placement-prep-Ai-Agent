from tools.retriever import retrieve_context

query="which companies require backend engineering and java?"
results=retrieve_context(query)
print("\nRetrived Documents:\n")
for doc in results:
    print(doc)
    print("-"*50)
    break