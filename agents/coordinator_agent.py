from agents.interview_agent import interview_agent
from agents.research_agent import research_agent
from agents.roadmap_agent import roadmap_agent

def coordinator_agent(user_query):
    context=research_agent(user_query)
    analysis=interview_agent(context)
    roadmap=roadmap_agent(analysis)

    return{
        "research":context,
        "analysis":analysis,
        "roadmap":roadmap
    }

