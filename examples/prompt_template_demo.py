from langchain_core.prompts import PromptTemplate
template=PromptTemplate.from_template(
    """
    analyze the following resume :
    
    {resume}
    """
)
prompt=template.invoke(
    {
        "resume":"Python ai projects"
    }
)
print (prompt.text)