# Rico

Rico is an AI-powered placement preparation assistant built using LangGraph, LangChain, ChromaDB, and Gemini.

I started this project primarily as a capstone-style learning project to understand how modern AI applications are built. The goal was to move beyond simple chatbot demos and learn concepts such as Agentic AI, multi-agent workflows, Retrieval-Augmented Generation (RAG), vector databases, prompt engineering, and LLM orchestration by applying them to a real problem.

Instead of building isolated examples for each concept, I wanted to integrate everything into a single application that could actually be useful for students preparing for placements and technical interviews.

---

## What Rico Does

A user uploads their resume and selects a target company.

Rico then:

* Analyzes the resume
* Identifies strengths and weaknesses
* Compares the profile against company-specific requirements
* Detects the Skill gap using a RAG pipeline backed by ChromaDB
* Generates a personalized preparation roadmap
* Creates Company specific interview questions
* Provides company-specific insights
* ATS-style analysis including keyword matching and resume recommendations

The final output is presented through a Streamlit dashboard.

---

## How It Works

Rico uses a multi-agent workflow built with LangGraph.

A resume is first analyzed and compared against company-specific information retrieved from a ChromaDB knowledge base. The outputs are then passed through multiple specialized agents responsible for gap analysis, ATS evaluation, roadmap generation, interview preparation, and company research before being combined into a final report.

---

## Tech Stack

### AI & Orchestration

* LangChain
* LangGraph
* Google Gemini

### Retrieval

* ChromaDB
* Retrieval-Augmented Generation (RAG)

### Frontend

* Streamlit

### Backend

* Python

---

## Running Locally

```bash
git clone <repo-url>
cd rico

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your-api-key
```

Build the knowledge base:

```bash
python ingest_documents.py
```

Run the application:

```bash
streamlit run app.py
```

---

# Developer's Note

This project was mainly an opportunity to gain hands-on experience with concepts such as Agentic AI, LangGraph, LangChain, RAG systems, vector databases, prompt engineering, and multi-agent workflows. More importantly, it helped me understand how these individual components can be combined into a complete, deployable application rather than existing as isolated examples.


ALSO LIVE DEMO -> https://rico-a-placement-prep-ai-agent-mzwxpf3usfqo4pabrkfqhr.streamlit.app/

(*do bear in mind , might take a while to bootup ,since there are multiple agents in play)
