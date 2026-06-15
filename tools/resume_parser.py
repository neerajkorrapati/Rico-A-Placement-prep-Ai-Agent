
#this is to read my resume.txt 

def read_resume(filepath):
    with open(filepath,"r",encoding="utf-8") as file:
        return file.read()