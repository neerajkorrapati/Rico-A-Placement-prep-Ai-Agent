import chromadb

client = chromadb.PersistentClient(
    path="data/chromadb"
)

collection = client.get_or_create_collection(
    name="company_knowledge"
)
def retrieve_context(query):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    documents = results["documents"][0]

    return documents