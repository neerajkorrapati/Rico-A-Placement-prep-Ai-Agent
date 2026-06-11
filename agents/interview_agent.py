from google import genai
from dotenv import load_dotenv

load_dotenv()

client=genai.Client()
def interview_agent(context):
    prompt=f"""
    Analyze the retrieved Context :
    {context}
    And identify the most important topics for Preparation.
    """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature":0.5,
            "max_output_tokens":500,
        }
    )
    return response.text