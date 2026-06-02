import json
def get_company_info(company_name):
    with open(
        "data/company_profiles.json","r") as file:
        database=json.load(file)
        print("Available companies:")
        print(database.keys())

        return database.get(company_name.lower(),"company not found in database")
