from agents.placement_prep_agent import placement_prep_agent

result = placement_prep_agent("data/sample_resume.txt","Amazon")
#this is to test the bug:->
#print(result)
#print(result.keys())
print("\n====RESUME ANALYSIS====\n")
print(
    result["resume_analysis"]
)
print("\n====GAP analysis =====\n")
print(result["gap_analysis"])
print("\n===Road Map===\n")
print(result["roadmap"])
print(type(result["resume_analysis"]))