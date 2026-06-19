from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt=PromptTemplate.from_template(
    """
    Research the company:

    {company}

    Return ONLY valid JSON.

    {{
        "company_overview":"",
        "tech_stack":[],
        "interview_focus":[]
    }}
    Do not rename keys.
        Do not add extra text.
        Return ONLY valid JSON.
        Do not add markdown.
        Do not add explanations.
        Do not rename keys.
    """
)
parser=JsonOutputParser();
chain=(prompt | llm | parser)

def company_research_agent(company):
    return chain.invoke({
        "company":company
    }
    )