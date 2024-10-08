import requests
import asyncio
import aiohttp
import patterns as pt

api = "https://pokeapi.co/api/v2/" #Definição das variáveis que a gente vai usar aqui
param_poke = "pokemon/"
poke_forms = list(range(10001, 10264))
pokes = list(range(1, 1026))
pokes.extend(poke_forms)

#Função pra formatar o json que recebemos em algo mais limpo
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
        'id': response['id'],
        'type': []
    }
    for i in response['types']:
        pokemon['type'].append(i['type']['name'])
    return pokemon

#Função que faz a requisição e chama a função de formatação
def get_poke(poke: str) -> dict:
    global api
    global param_poke
    response = requests.get(api + param_poke + poke).json()
    pokemon = format_poke(response)

    return pokemon

#Aqui começa a gambiarra das funções assíncronas, não vou conseguir explicar porque não entendi ainda

def get_tasks(session):
    tasks = []

    if len(pokes) > 100:
        sublists = [pokes[i:i + 100] for i in range(0, len(pokes), 100)]

        for sublist in sublists:
            result = []
            for i in sublist:
                result.append(session.get(api + param_poke + str(i), ssl=False))

            tasks.append(result)
        return tasks
    else:
        for i in pokes:
            tasks.append(session.get(api + param_poke + str(i), ssl=False))
        return tasks

def get_tasks_filter(session, dex):
    tasks = []

    if len(dex) > 100:
        sublists = [dex[i:i + 100] for i in range(0, len(dex), 100)]

        for sublist in sublists:
            result = []
            for i in sublist:
                result.append(session.get(i['species']['url'], ssl=False))

            tasks.append(result)
        return tasks
    else:
        for i in dex:
            tasks.append(session.get(i['species']['url'], ssl=False))
        return tasks

async def get_pokequests(filter: bool, results: list, dex = None):
    if filter:
        async with aiohttp.ClientSession() as session:
            tasks = get_tasks_filter(session, dex)
            if len(tasks) > 1:
                for i in tasks:
                    responses = await asyncio.gather(*i)
                    for response in responses:
                        results.append(await response.json())
            else:
                responses = await asyncio.gather(*tasks)
                for response in responses:
                    results.append(await response.json())
    else:
        async with aiohttp.ClientSession() as session:
            tasks = get_tasks(session)
            if len(tasks) > 1:
                for i in tasks:
                    responses = await asyncio.gather(*i)
                    for response in responses:
                        results.append(await response.json())
            else:
                responses = await asyncio.gather(*tasks)
                for response in responses:
                    results.append(await response.json())
#Aqui acaba a gambiarra

def get_pokedex(filter: bool, dex = None): #Essa função serve pra chamar as funções assíncronas
    results = []
    if filter:
        asyncio.run(get_pokequests(filter, results, dex))
        return results
    else:
        asyncio.run(get_pokequests(filter, results))
        return results

def filter_gen(dex: list, filter_value: str):
    response = []
    
    if filter_value == 'All':
        for i in range(1, 1026):
            response.append(dex[i-1])
    else:
        filter_value = filter_value.split()
        for key, value in pt.generations.items():
            if int(filter_value[1]) == int(key):
                for i in range(value[0], (value[1]+1)):
                    response.append(dex[i-1])

    return response

def filter_type(dex: list, filter_value: str):
    response = []

    if filter_value == 'All':
        response = dex
    else:
        for i in dex:
            for j in i['types']:
                if j['type']['name'].capitalize() == filter_value:
                    response.append(i)

    return response

#Isso servia pra eu saber se tava funcionando, pode ignorar
# for i in results:
#     print(f'{i['name']} - {i['id']}')