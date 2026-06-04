from dotenv import load_dotenv
from google import genai
load_dotenv()

client=genai.Client()

def rewrite_query(user_query,chat_history):
    prompt=f"""conversation history:{chat_history}, 
     current user Question: {user_query},

     Rewrite this into a single standalone search query.
     only return the the rewritten query.
     don't explain anything else.
       """
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
