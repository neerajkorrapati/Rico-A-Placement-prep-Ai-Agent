from google import gemini
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
def roadmap_agent(topics):
    prompt=f"""
    from the given topics below :
    {topics}
    create a 4- Week preperation roadmap.
    """

    response=client.models.generate_content(
        models="gemini-2.5-flash",
        content=prompt,
        config={
            "temperature":0.7,
        }
    )

    return response.text
