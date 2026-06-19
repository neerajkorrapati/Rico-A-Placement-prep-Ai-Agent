from google import genai
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=PromptTemplate.from_template(
    """
    you are an interview preperation expert.
        Company: {company},

        Gap analysis:{gap_analysis}
        Generate interview Questions.
        Return ONLY valid JSON.

        Use EXACTLY this format:

        {{
            "dsa":[],
            "system_design":[],
            "behavioral":[]
        }}

        Do not rename keys.
        Do not add extra text.
        Return ONLY valid JSON.
        Do not add markdown.
        Do not add explanations.
        Do not rename keys.
     """
)
parser =JsonOutputParser()
chain =(prompt | llm | parser)
def interview_agent(gap_analysis,company):
    return chain.invoke({

        "gap_analysis":gap_analysis,
        "company":company
    }
    )
