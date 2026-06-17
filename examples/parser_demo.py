from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()
result=parser.invoke(
    "Hello this is a test"
)
print(result)