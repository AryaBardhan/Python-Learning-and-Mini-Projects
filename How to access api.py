import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200: # here 200 is a response code for api like error 404 which is used for file not found, here 200 means successful
        pokemon_data = response.json() #we taking the  response data into a json string format here
        print("Data retrieved!")
        return pokemon_data
    else:
        print("Failed to retrieve the data")

pokemon_name = "charizard"
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name: {pokemon_info["name"]}") # to access the value of a dictionary by a key
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
