from tools.resume_parser import read_resume

from agents.resume_agent import (
    resume_agent
)

resume = read_resume(
    "data/sample_resume.txt"
)

result = resume_agent(
    resume
)

print(type(result))
print(result)