from agents.coordinator_agent import coordinator_agent

result=coordinator_agent("Help me prepare for Amazon interviews")
print("\n===RESEARCH_AGENT==\n")
print(result["research"])
print("\n===INTERVIEW AGENT==\n")
print(result["analysis"])

print("\n===ROADMAP_AGENT==\n")
print(result["roadmap"])
