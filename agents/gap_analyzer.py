from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt=PromptTemplate.from_template(
    """
You are a career Advisor.
    Resume analysis:
    {resume_analysis},

    company Requirements:
    {company_context},
    i want you to give me output in a strick JSON format.
    the format i want you to strictly follow:
    {{
    "covered_skills":[],
    "missing_skills":[],
    "recommendations":[],
    "skill_gap":[]
    }}
    i also want you to keep the response as concise as possible, and adhere to this format strictly
    """
)
parser=JsonOutputParser()
chain=(prompt | llm | parser)
def gap_analyzer(company_context,resume_analysis):
    return chain.invoke({
        "company_context":company_context,
        "resume_analysis":resume_analysis
    }        
    )
