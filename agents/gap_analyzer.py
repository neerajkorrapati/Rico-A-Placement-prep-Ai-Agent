from dotenv import load_dotenv
from google import genai

load_dotenv()
client=genai.Client()
def gap_analyzer(company_context,resume_analysis):
    prompt=f"""
    You are a career Advisor.
    Resume analysis:
    {resume_analysis},

    company Requirements:
    {company_context},

    i need you to identify:
    1.the skills already covered,
    2.missing skills
    3.most important skill gaps,
    4.improvement reccomendations

    i also want you to keep the response as concise and small as possible.
    """
    response= client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text