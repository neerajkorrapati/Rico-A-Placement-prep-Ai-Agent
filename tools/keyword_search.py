def keyword_search(query):
    #this is my keyword retrieving tool
    with open("data\company_notes.txt","r",encoding="utf-8") as file:
        text=file.read()
    matches=[]

    for line in text.split("\n"):
        if(query.lower() in line.lower()):
            matches.append(line)
    
    return matches