from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
template=PromptTemplate.from_template(
    """
    Analyze the given topic in less than 30 words, while giving a definite answer:
    {topic}
    """
)
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()
#this is where we be building our first chain 
chain=(template | llm | parser)
result=chain.invoke(
    {
    "topic":"the best looking car of all time. with model and make."
    }
)
print(result)