from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=PromptTemplate.from_template(
    """
    You are an ATS resume Screening system.

    Resume Analysis:{resume_analysis}

    Gap Analysis: {gap_analysis}

    Return ONLY valid JSON.

    Use EXACTLY this format:

    {{
        "ats_score":0,
        "keyword_match":0,
        "missing_keywords":[],
        "recommendations":[]
    }}

    Rules:
    - ats_score must be between 0 and 100
    - keyword_match must be between 0 and 100
    - Do not add extra keys
    - Do not add markdown
    """
)
parser=JsonOutputParser()
chain=(prompt | llm | parser)
def ats_agent(resume_analysis,gap_analysis):
    return chain.invoke(
    {
        "resume_analysis":resume_analysis,
        "gap_analysis":gap_analysis
    }
    )