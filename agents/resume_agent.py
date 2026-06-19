from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser #changed from str output parser to JSON output parser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt=PromptTemplate.from_template(
    """
    I need you to analyze this resume,
        Return only Valid JSON format:
        the format:
        {{
        "technical_skills":[],
        "strengths":[],
        "weaknesses":[],
        "improvements":[]
        }}
        make sure u use these exact key names, do not rename any of the keys.
        Resume:
        {resume_text}.

        Do not rename keys.
        Do not add extra text.
        Return ONLY valid JSON.
        Do not add markdown.
        Do not add explanations.
        Do not rename keys.
    """
)
parser=JsonOutputParser()
chain=(prompt | llm | parser)
#this modified fcuntion now only uses langchain as compared to before:
def resume_agent(resume_text):
    return chain.invoke({
        "resume_text":resume_text
    })
    