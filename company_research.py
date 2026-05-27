import json
from dotenv import load_dotenv
from google import genai
from pydantic import ValidationError

from models.company import CompanyProfile
from tools.parser import clean_markdown_json

# Load .env variables
load_dotenv()

# Create Gemini client
client = genai.Client()

# System instruction
SYSTEM_PROMPT = """
You must respond ONLY with valid JSON.

Required structure:

{
    "company_name": "Company Name",
    "tech_stack": ["Python", "Kafka"],
    "difficulty_rating": "Medium",
    "interview_rounds": [
        {
            "round_number": 1,
            "round_name": "Online Assessment",
            "format": "Coding Test",
            "focus_areas": ["DSA", "Arrays"]
        }
    ]
}
"""


def get_company_profile(company_name: str) -> CompanyProfile:

    # Retry loop
    for attempt in range(3):

        try:

            print(f"\nAttempt {attempt + 1}...\n")

            # Gemini API call
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Generate an SDE-1 interview profile for {company_name}.",
                config={
                    "system_instruction": SYSTEM_PROMPT,
                    "temperature": 0.3,
                }
            )

            # Raw text output
            raw_text = response.text

            print("RAW MODEL OUTPUT:\n")
            print(raw_text)
            print("\n-------------------------\n")

            # Clean markdown
            cleaned_json = clean_markdown_json(raw_text)

            # Convert JSON string → Python dictionary
            parsed_data = json.loads(cleaned_json)

            # Validate using Pydantic
            validated_profile = CompanyProfile(**parsed_data)

            return validated_profile

        except json.JSONDecodeError as e:
            print(f"JSON Parsing Error: {e}")

        except ValidationError as e:
            print(f"Pydantic Validation Error:\n{e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    raise Exception("Failed after 3 attempts.")


if __name__ == "__main__":

    try:

        profile = get_company_profile("Flipkart")

        print("\nVALIDATED COMPANY PROFILE:\n")

        print(profile.model_dump_json(indent=2))

    except Exception as e:
        print(f"\nFINAL FAILURE: {e}")