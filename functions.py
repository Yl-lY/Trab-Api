import requests
import asyncio
import aiohttp
import time

api = "https://pokeapi.co/api/v2/"
param_poke = "pokemon/"
pokes = list(range(1, 1001))

def format_poke(response):
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
        'generation': lambda x: requests.get(response['species']['url'].json()['generation']['name']),
        'type': []
    }
    for i in response['types']:
        pokemon['type'].append(i['type']['name'])
    return pokemon

def get_poke(poke: str) -> dict:
    global api
    global param_poke
    response = requests.get(api + param_poke + poke).json()
    pokemon = format_poke(response)

    return pokemon

results = []
start = time.time()
def get_tasks(session):
    tasks = []

    if len(pokes) > 100:
        sublists = [pokes[i:i + 100] for i in range(0, len(pokes), 100)]

        for sublist in sublists:
            result = []
            for i in sublist:
                result.append(session.get(api + param_poke + str(i), ssl=False))
                # tasks.append(session.get(api + param_poke + str(i), ssl=False))
            tasks.append(result)
        return tasks
    else:
        for i in pokes:
            tasks.append(session.get(api + param_poke + str(i), ssl=False))
        return tasks
        
async def get_pokequests():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        if len(tasks) == 10:
            for i in tasks:
                responses = await asyncio.gather(*i)
                for response in responses:
                    results.append(await response.json())
        else:
            responses = await asyncio.gather(*tasks)
            for response in responses:
                results.append(await response.json())

def get_pokedex():
    asyncio.run(get_pokequests())
    return results
end = time.time()



print(end - start)
for i in results:
    print(f'{i['name']} - {i['id']}')