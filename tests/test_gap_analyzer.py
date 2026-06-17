from tools.resume_parser import read_resume

from agents.resume_agent import (
    resume_agent
)

from agents.gap_analyzer import (
    gap_analyzer
)

resume = read_resume(
    "data/sample_resume.txt"
)

resume_analysis = resume_agent(
    resume
)

company_context = """
Amazon wants:
AWS,
System Design,
Distributed Systems
"""

result = gap_analyzer(
    company_context,
    resume_analysis
)

print(type(result))
print(result)