from dotenv import load_dotenv
from google import genai

load_dotenv()
client=genai.Client()

def road_map_agent(gap_analysis_result):
    prompt=f"""
    You are an interview preparation coach.
    
    The following gap analysis was generated for 
    a student preparing for his placements:
    {gap_analysis_result}
    1.Create a 4-week Roadmap
    2.Focus on missing skills first
    3.Give weekly goals
    4.Prioritize high-impact topics 
    
    keep the routine as practical as possible.
    also keep the response as short and concise as possible.
    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text