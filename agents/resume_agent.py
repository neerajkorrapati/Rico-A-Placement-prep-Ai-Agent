from dotenv import load_dotenv
from google import genai
load_dotenv()

client=genai.Client()

def analyze_resume(resume_text):
    prompt=f"""
    I need you to analyze this resume,
    identify the following:
    1. Strengths,
    2. Weaknesses,
    3. Suggested Improvements,
    4.Technical skills,

    keep the response as concise and small as possible.
    The resume:
    {resume_text}.
    also print the the first few points of resume, 
    and give respones based off the topics present in the resume uploaded only.
    """

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text