from dotenv import load_dotenv
import json
from google import genai
from tools.calculator import calculator
from tools.datetime_tool import get_current_time
from tools.file_reader import read_file
from tools.parser import clean_markdown_json
from tools.company_lookup import get_company_info  
from tools.retriever import retrieve_context
from tools.query_rewritter import rewrite_query
load_dotenv()
client= genai.Client()

chat_history=[]
def formatted_chat_history(chat_history): #here we convert and store the chat historyy in a formatted json format.
    formatted=""
    for message in chat_history:
        formatted+=(
            f"{message['role']}: "
            f"{message['content']}\n"
        )
    return formatted

SYSTEM_PROMPT=""" 
you are a routing agent.
available tools:
1.calculator: used for mathematical calculations.
2.datetime_tool: used for getting the current time.

3. file_reader: which is used for reading the content of a file.

4.company_lookup: used for getting company information from a local data_base.

5.retriever : used for searching up company interview knowledge base, and other information like ashwath and madhavan. answer only using the retrieved context, if the answer not present , then say :"Information not available in knowledge base".

6.General fallback: if query is not related to any of the above, use retriever tool and check if information is in the knowledge base, if not there then say:"Information not available in knowledge base.

example:
{
"tool":"calculator",
"input":"2+3*12"
}
example:
{
"tool":"retriever",
"input":"Amazon focus"
}
Respond only with valid JSON object.
Do not explain.
Do not use markdown.
Do not wrap JSON in ```json blocks.

Example:

{
    "tool": "calculator",
    "input": "2+3*12"
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
    elif(tool_name=="company_lookup"):
        return get_company_info(tool_input)
    elif(tool_name=="retriever"):
       # return retrieve_context(tool_input)  #make changeshere for search_history context retrieval
       formatted_history =formatted_chat_history(chat_history)
       search_query=rewrite_query(tool_input,formatted_history)
       print(f"\nRewritten Query{search_query}")

       return retrieve_context(search_query)
    
    else:
        return "Invalid tool specified."

def generate_final_response(user_request:str,tool_result:str):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"User request:{user_request}, tool result:{tool_result}. Provide a helpful response to the user.keep it less than 30 words",
        config={
            "temperature":0.1,
        }
    )
    return response.text

if __name__=="__main__":
   print("\n Placement Prep Agent:\n")
   print("Type 'exit' to quit.\n")
   while(True):
       user_request= input("You: ")
       if(user_request.lower()=="exit"):
           break
       try:
           chat_history.append({
               "role":"user",
               "content":user_request
           })
           result=decide_tool(user_request)
           print("Router ouput\n")
           print(result)
           decision=parse_tool_decision(result)
           tool_result=execute_tool(decision)
           final_response=generate_final_response(user_request,tool_result)
           print(f"Agent final response: {final_response}.\n")

           chat_history.append({
               "role":"assistant",
               "content":final_response
           })

           #keep only the last10 messages of chat history;

           chat_history[:]=chat_history[-10:]

       except Exception as e:
           print(f"Error: {e}")
    


    

