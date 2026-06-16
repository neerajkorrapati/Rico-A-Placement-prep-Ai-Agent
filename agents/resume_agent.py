from dotenv import load_dotenv
from google import genai
from tools.parser import clean_markdown_json
import json
load_dotenv()

client=genai.Client()

def analyze_resume(resume_text):
    prompt=f"""
    I need you to analyze this resume,
    Return only Valid JSON format:
    the format:
    {{
      "technical_skills":[],
      "strengths":[],
      "weaknesses":[],
      "improvements":[]
    }}
    make sure u use these exact key names, do not rename any of the keys.
    Resume:
    {resume_text}.
    """

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    cleaned = clean_markdown_json(response.text)

    return json.loads(cleaned)