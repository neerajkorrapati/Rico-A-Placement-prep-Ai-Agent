from dotenv import load_dotenv
from google import genai
load_dotenv()

client=genai.Client()

def analyze_resume(resume_text):
    prompt="""
    I need you to analyze this resume,
    identify the following:
    1. Strengths,
    2. Weakness,
    3. Improvements,
    4.Technical skills,

    i want you to briefly summarize and mention all of the above points, while using the tokens of the api as resourcefully as possible.
    The resume:
    {resume_text}.
    """

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text