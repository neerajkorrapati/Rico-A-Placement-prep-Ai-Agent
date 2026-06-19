from tools.resume_parser import read_resume

from agents.placement_graph import (
    workflow
)

resume = read_resume(
    "data/sample_resume.txt"
)

result = workflow.invoke(
    {
        "resume_text": resume,
        "company": "Amazon"
    }
)

print(result.keys())

print(result["resume_analysis"])

print(result["gap_analysis"])

print(result["roadmap"])