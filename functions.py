import requests

api = "https://pokeapi.co/api/v2/"
param_poke = "pokemon/"

def get_poke(poke: str) -> dict:
    global api
    global param_poke
    response = requests.get(api + param_poke + poke).json()
    pokemon = {
        'name': response['name'],
        'sprite': {
            'front': response['sprites']['front_default'],
            'back': response['sprites']['back_default'],
            'front_shiny': response['sprites']['front_shiny'],
            'back_shiny': response['sprites']['back_shiny']
        },
        'sprite_female':{
            'front': response['sprites']['front_female'],
            'back': response['sprites']['back_female'],
            'front_shiny': response['sprites']['front_shiny_female'],
            'back_shiny': response['sprites']['back_shiny_female']
        },
        'type': []
    }
    for i in response['types']:
        pokemon['type'].append(i['type']['name'])

    return pokemon