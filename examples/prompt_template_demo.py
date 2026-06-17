from langchain_core.prompts import PromptTemplate

template= PromptTemplate.from_template(
"""
Analyze the following resume :

{resume}
"""
)
prompt=template.invoke(
    {
    "resume":"Python AI Projects" #here langchain replaces resume in the above prompt_template with Python ai projects
    }
)
print(prompt.text)
