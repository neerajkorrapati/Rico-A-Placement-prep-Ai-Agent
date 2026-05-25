import os
from dotenv import load_dotenv
from google import genai
from colorama import Fore, Style, init
#chatbot_py
# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client()

# Conversation history
chat_history = []

# System instruction
SYSTEM_PROMPT = """
You are a helpful AI mentor teaching a student Agentic AI engineering.
Keep explanations beginner-friendly but technically accurate.
"""

print(Fore.CYAN + "\n=== Gemini AI Chatbot ===")
print(Fore.YELLOW + "Type 'exit' to quit.\n")

while True:

    # User input
    user_input = input(Fore.GREEN + "You: ")

    if user_input.lower() == "exit":
        print(Fore.RED + "\nGoodbye!")
        break

    # Add user message to history
    chat_history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )

    try:

        # Streaming response
        response_stream = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=chat_history,
            config={
                "system_instruction": SYSTEM_PROMPT,
                "temperature": 0.7,
                "max_output_tokens": 500,
            }
        )

        print(Fore.BLUE + "\nGemini: ", end="")

        full_response = ""

        # Stream tokens/chunks live
        for chunk in response_stream:

            if chunk.text:
                print(chunk.text, end="", flush=True)
                full_response += chunk.text

        print("\n")

        # Save assistant response into memory
        chat_history.append(
            {
                "role": "model",
                "parts": [{"text": full_response}]
            }
        )

    except Exception as e:
        print(Fore.RED + f"\nError: {e}\n")