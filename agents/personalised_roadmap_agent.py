from dotenv import load_dotenv
from google import genai
import json
from tools.parser import clean_markdown_json


load_dotenv()
client=genai.Client()

def road_map_agent(gap_analysis_result):
    prompt=f"""
    You are an interview preparation coach.
    
    The following gap analysis was generated for 
    a student preparing for his placements:
    {gap_analysis_result}
    Create a 4-week preparation roadmap.
i want you to return me the answer in a structured JSON Format .
the format:
{{
  "week_1":[],
  "week_2":[],
  "week_3":[],
  "week_4":[]
}}
also do not rename the keys
    
    keep the routine as practical as possible.
    also keep the response as short and concise as possible.
    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    cleaned=clean_markdown_json(response.text)
    return json.loads(cleaned)