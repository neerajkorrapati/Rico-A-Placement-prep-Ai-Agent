from dotenv import load_dotenv
import json
from google import genai
from tools.calculator import calculator
from tools.datetime_tool import get_current_time
from tools.file_reader import read_file
from tools.parser import clean_markdown_json
load_dotenv()
client= genai.Client()
SYSTEM_PROMPT=""" 
you are a routing agent.
available tools:
1.calculator: used for mathematical calculations.
2.datetime_tool: used for getting the current time.

3. file_Reader: which is used for reading the content of a file.
respond only with valid JSON .

example:
{
"tool":"calculator",
"input":"2+3*12"
}
"""

def decide_tool(user_input:str):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config={
            "system_instruction": SYSTEM_PROMPT,
            "temperature":0,
        }
    )
    return response.text
def  parse_tool_decision(response_text:str):
    cleaned = clean_markdown_json(response_text)
    return json.loads(cleaned)#returns a python dictionary (dict)

def execute_tool(decision:dict):
    tool_name=decision.get("tool")
    tool_input=decision.get("input")
    print(f"Executing {tool_name} with input: {tool_input}")

    if(tool_name=="calculator"):
        return calculator(tool_input)
    elif(tool_name=="datetime_tool"):
        return get_current_time()
    elif(tool_name=="file_reader"):
        return read_file(tool_input)
    else:
        return "Invalid tool specified."

def generate_final_response(
        user_request:str,
        tool_result:str
):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"User request:{user_request}, tool result:{tool_result}. Provide a helpful response to the user."
    ) 
    return response.text

if __name__=="__main__":
    user_request=input("enter your request: ")
    result=decide_tool(user_request)
    print(result)
    decision=parse_tool_decision(result)
    execution_result=execute_tool(decision)
    print(f"Tool execution result: {execution_result}")

    final_response=generate_final_response(user_request,execution_result)
    print(final_response)

