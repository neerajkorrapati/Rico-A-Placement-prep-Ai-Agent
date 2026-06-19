import chromadb
#Create Chroma Client
client = chromadb.PersistentClient(
    path="data/chromadb"
)
collection = client.get_or_create_collection(
    name="company_knowledge"
)
# Clear Existing Data
existing = collection.get()

if existing["ids"]:
    collection.delete(ids=existing["ids"])

# Load Company Notes
with open(
    "data/company_notes.txt",
    "r",
    encoding="utf-8"
) as file:

    text = file.read()

# Split Documents By Company
companies = text.split("Company:")
count = 0
for i, company_text in enumerate(companies):
    company_text = company_text.strip()

    if not company_text:
        continue

    lines = company_text.split("\n")
    company_name = lines[0].strip()

    collection.add(
        documents=[company_text],
        ids=[f"company_{i}"],

        metadatas=[
            {
                "company": company_name
            }
        ]
    )
    count += 1
# Summary
print(f"Successfully ingested {count} companies into ChromaDB.")
print(f"Collection now contains {collection.count()} documents.")