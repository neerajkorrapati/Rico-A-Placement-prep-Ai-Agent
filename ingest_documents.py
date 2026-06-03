import chromadb
#this creates chromadb which stores vectors/ 
client=chromadb.PersistentClient(path="data/chromadb")
collection=client.get_or_create_collection(name="company_knowledge")
#load the documents:
with open("data/company_notes.txt","r",encoding="utf-8") as file:
    text=file.read()
documents = text.split("\n\n") #split by double newlines to get chunks of data;

for i, doc in enumerate(documents):
    collection.add(
        documents=[doc],
        ids=[f"doc_{i}"]
    )
print("items succesfully ingested into chromadb")
    #on running above, chromadb ingests the documents and creates vector embeddings for each document.
