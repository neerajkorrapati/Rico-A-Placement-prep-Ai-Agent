from dotenv import load_dotenv
import json
from google import genai
from tools.parser import clean_markdown_json

load_dotenv()
client=genai.Client()
def gap_analyzer(company_context,resume_analysis):
    prompt=f"""
    You are a career Advisor.
    Resume analysis:
    {resume_analysis},

    company Requirements:
    {company_context},
    i want you to give me output in a strick JSON format.
    the format i want you to strictly follow:
    {{
    "covered_skills":[],
    "missing_skills":[],
    "recommendations":[],
    "skill_gap":[]
    }}
    

    i also want you to keep the response as concise as possible, and adhere to this format strictly
    """
    response= client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    cleaned= clean_markdown_json(response.text)
    return json.loads(cleaned.text)