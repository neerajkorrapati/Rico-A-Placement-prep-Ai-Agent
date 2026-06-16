from google import genai
from dotenv import load_dotenv
import json
from tools.parser import clean_markdown_json
load_dotenv()

client = genai.Client()

def roadmap_agent(topics):

    prompt = f"""
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
Topics:

{topics}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    cleaned=clean_markdown_json(response.text)
 
    return json.loads(cleaned)