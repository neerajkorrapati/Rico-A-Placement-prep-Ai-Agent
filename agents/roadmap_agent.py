from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def roadmap_agent(topics):

    prompt = f"""
Create a 4-week preparation roadmap.

Topics:

{topics}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text