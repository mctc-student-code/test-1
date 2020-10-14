import requests

url = "https://rapidapi.p.rapidapi.com/parser"

querystring = {"ingr":"orange"}

headers = {
    'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com",
    'x-rapidapi-key': "d23a64a751mshdd23887198cf520p1987fcjsnec0a158fba6f"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

calories = response["parsed"][0]['food']['nutrients']['ENERC_KCAL']
protein = response["parsed"][0]['food']['nutrients']['PROCNT']
fat = response["parsed"][0]['food']['nutrients']['FAT']
carbohydrates = response["parsed"][0]['food']['nutrients']['CHOCDF']
fiber = response["parsed"][0]['food']['nutrients']['FIBTG']
print(f'Calories:  {calories}  |  Protein:  {protein}  |  Fat:  {fat}  |  Carbohydrates:  {carbohydrates}  |  Fiber:  {fiber}')