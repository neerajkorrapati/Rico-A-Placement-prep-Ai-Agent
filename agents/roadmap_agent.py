from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
prompt=PromptTemplate.from_template(
    """
    You are an interview preparation coach.
    
    The following gap analysis was generated for 
    a student preparing for his placements:
    {gap_analysis_result}
    Create a 4-week preparation roadmap.
    i want you to return me the answer in a structured JSON Format .
    the format:
    {{
    "week_1":[],
    "week_2":[],
    "week_3":[],
    "week_4":[]
    }}
    also do not rename the keys
        
        keep the routine as practical as possible.
        also keep the response as short and concise as possible.
    """
)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=JsonOutputParser()
chain=(prompt|llm|parser)
def roadmap_agent(gap_analysis_result):
    return chain.invoke({
        "gap_analysis_result":gap_analysis_result
    })
