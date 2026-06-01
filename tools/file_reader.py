def read_file(filename:str):
    try:
        with open(filename,'r') as file:
            return file.read()
    except Exception as e:
        return f"Error :{e}"
