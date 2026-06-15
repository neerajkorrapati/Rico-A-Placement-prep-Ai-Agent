from tools.resume_parser import read_resume
from agents.resume_agent.py import analyze_resume

resume = read_resume("data\sample_resume.txt")

result=analyze_resume(resume)
print(result)
