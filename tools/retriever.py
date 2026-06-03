import chromadb

client=chromadb.PersistentClient(path="data/chromadb")

collection=client.get_collection("company_knowledge")

def retrieve_context(query):
    results=collection.query(
        query_texts=[query],
        n_results=2
    )
    return results['documents'][0]
