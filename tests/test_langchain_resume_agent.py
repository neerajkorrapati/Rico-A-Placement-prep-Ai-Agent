from tools.resume_parser import read_resume

from agents.resume_agent_langchain import (
    resume_agent_langchain
)

resume = read_resume(
    "data/sample_resume.txt"
)

result = resume_agent_langchain(
    resume
)

print(type(result))
print(result)