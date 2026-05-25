import os
import re
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file
load_dotenv()

def clean_markdown_json(raw_text: str) -> str:
    """Strips away ```json ... ``` code blocks to isolate the raw JSON."""
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return raw_text.strip()




def get_company_profile(company_name: str) -> dict:
    """Asks Gemini for a company profile and parses it into a dictionary."""
    # Instantiates the client (picks up GEMINI_API_KEY from your .env file)
    client = genai.Client()

    system_instruction = """
    You must output your response ONLY as a single valid JSON object.
    Do not write any introductory or concluding text. Do not explain anything.
    
    Required JSON Structure:
    {
        "company_name": "Company Name",
        "tech_stack": ["Tech1", "Tech2"],
        "difficulty_rating": "Medium",
        "interview_rounds": [
            {
                "round_number": 1,
                "round_name": "Round Name",
                "format": "e.g., Coding Test",
                "focus_areas": ["Topic1", "Topic2"]
            }
        ]
    }
    """



    response = client.models.generate_content(
        model='gemini-2.5-flash', # fast, cost-effective model
        contents=f"Provide a placement preparation profile for {company_name} SDE-1.",
        config={"system_instruction": system_instruction}
    )

    raw_text = response.text
    print("\n--- DEBUG: RAW MODEL OUTPUT ---")
    print(raw_text)
    print("--------------------------------\n")

    # Clean the string and parse it directly into a Python dictionary
    json_string = clean_markdown_json(raw_text)
    parsed_data = json.loads(json_string)
    
    return parsed_data

if __name__ == "__main__":
    print("Connecting to Gemini...")
    try:
        profile = get_company_profile("Flipkart")
        print("Success! Parsed output:")
        print(json.dumps(profile, indent=2))
    except Exception as e:
        print(f"Failed to parse: {e}")