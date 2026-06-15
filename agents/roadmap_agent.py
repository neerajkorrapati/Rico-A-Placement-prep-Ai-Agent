from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def roadmap_agent(topics):

    prompt = f"""
Create a 4-week preparation roadmap.
Keep it precise and concise, in order to avoid using excess tokens 
and resources.

Topics:

{topics}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text