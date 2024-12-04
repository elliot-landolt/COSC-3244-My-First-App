import requests

def get_drinks():
    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"

    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the drink names and thumbnail URLs
        drinks = [{"name": drink["strDrink"], "thumbnail": drink["strDrinkThumb"]} for drink in data["drinks"][:20]]
        return drinks
