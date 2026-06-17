from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

template=PromptTemplate.from_template(
    """
    Explain the following topic in 40-50 words(mention horsepower and torque as well),along with the estimated time it would take it to do a 
    lap in the BUDDH international circuit, also compare it to the time it would take a lamborghini huracan:
    {topic}
    """
)
prompt=template.invoke(
    {
        "topic":"Baleno -2015 petrol 1.2"
    }
)
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
response=llm.invoke(prompt)
print(response.text)