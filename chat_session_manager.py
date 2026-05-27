import json
import uuid
from pathlib import Path

from dotenv import load_dotenv
from google import genai
# Load environment variables
load_dotenv()

# Gemini client
client = genai.Client()
# Session storage directory
SESSIONS_DIR = Path("data/sessions")
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

# Create unique session ID
def create_new_session() -> str:
    session_id = str(uuid.uuid4())
    return session_id
# Get JSON filepath for session
def get_session_filepath(session_id: str) -> Path:
    return SESSIONS_DIR / f"{session_id}.json"

# Save chat history
def save_session(session_id: str, chat_history: list):
    filepath = get_session_filepath(session_id)
    with open(filepath, "w") as file:
        json.dump(chat_history, file, indent=2)


# Load chat history
def load_session(session_id: str) -> list:

    filepath = get_session_filepath(session_id)
    if not filepath.exists():
        return []
    with open(filepath, "r") as file:
        return json.load(file)


# Keep only recent messages
def trim_chat_history(chat_history: list, max_messages: int = 10):
    return chat_history[-max_messages:]

# Main chatbot loop
if __name__ == "__main__":

    # Create session
    session_id = create_new_session()
    print(f"\nSESSION ID: {session_id}")

    # Load old memory if exists
    chat_history = load_session(session_id)
    print("\nPersistent Gemini Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        # User input
        user_input = input("You: ")
        # Exit condition
        if user_input.lower() == "exit":
            break
        # Store user message
        chat_history.append(
            {
                "role": "user",
                "parts": [{"text": user_input}]
            }
        )
        # Trim memory
        chat_history = trim_chat_history(chat_history)

        # Gemini API call
        response_stream = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=chat_history,
            config={
                "temperature": 0.7,
                "max_output_tokens": 500,
            }
        )
        print("\nGemini: ", end="")

        full_response = ""
        # Stream response
        for chunk in response_stream:

            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_response += chunk.text

        print("\n")
        # Save model response into memory
        chat_history.append(
            {
                "role": "model",
                "parts": [{"text": full_response}]
            }
        )
        # Save session to disk
        save_session(session_id, chat_history)