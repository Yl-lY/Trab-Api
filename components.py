import flet as ft
import patterns as pt
import functions as func

# Função para criação da nossa barra de navegação
def create_nav_bar(func_name):
    navigation_bar = ft.NavigationBar(
        destinations=[
        ft.NavigationDestination(icon_content=pt.navigation_icon_pokemon, selected_icon_content=pt.navigation_icon_pokemon_activated, label='Pokémon'),
        ft.NavigationDestination(icon_content=pt.navigation_icon_pokedex, selected_icon_content=pt.navigation_icon_pokedex_activated, label='Pokédex'),
        ft.NavigationDestination(icon_content=pt.navigation_icon_moves, selected_icon_content=pt.navigation_icon_moves_activated, label='Fazendo...')
        ],
        on_change= func_name,
        selected_index=1
    )
    return navigation_bar

#Função para criação da barra de busca
def search_bar(func_name, align = ft.MainAxisAlignment.START):
    search_bar = ft.Row(
        controls=[
            ft.TextField(label='Pokémon', on_submit=func_name),
            ft.ElevatedButton(content=ft.Icon(name=ft.icons.SEARCH_ROUNDED), on_click=func_name)
        ],
        alignment= align
    )
    return search_bar

#Função para criar os dropdowns que irão filtrar os pokémon
def filter_bar(dex, load_func) -> ft.Row:
    def funcao_top(e, dex):
        gen = generation_dropdown.value
        tp = type_dropdown.value

        new_dex = func.filter_gen(dex, gen)
        new_dex = func.filter_type(new_dex, tp)

        load_func(new_dex)

    load_button = ft.Container(content=ft.Icon(name=ft.icons.CATCHING_POKEMON, color='white', size=35),border_radius = ft.border_radius.all(100), on_click= lambda e: funcao_top(e, dex))

    generation_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option('All', alignment=ft.alignment.center)
            ]
        )
    for i in range(1,10):
        generation_dropdown.options.append(ft.dropdown.Option(f'Geração ' + str(i), alignment=ft.alignment.center))

    type_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option('All', alignment=ft.alignment.center)
        ]
    )
    for key in pt.type_color:
        type_dropdown.options.append(ft.dropdown.Option(key.capitalize(), alignment=ft.alignment.center))
    
    generation_dropdown.value, type_dropdown.value = 'All', 'All'
    bar = ft.Row(
        vertical_alignment= ft.CrossAxisAlignment.CENTER,
        alignment= ft.MainAxisAlignment.CENTER,
        controls=[
            load_button,
            generation_dropdown,
            type_dropdown,
            ft.Text(color='white', text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_500)
        ]
    )
    for i in bar.controls:
        if i == load_button:
            i.bgcolor = 'red'
            i.padding = ft.padding.all(1)
        else:
            i.height = 40
            i.width = 100
            i.bgcolor = 'black'
            i.alignment = ft.alignment.center
            i.border_color = 'red'
            i.color = 'white'
            i.border_radius = ft.border_radius.all(15)
            i.content_padding = ft.padding.all(0)
            i.text_style = ft.TextStyle(weight=ft.FontWeight.BOLD)
        
    return bar

#Função teste do evento on_click para container
def poke_body(e: ft.ControlEvent, name):
    print(f'{e.data} - {name}')

#Função para criar os cards de pokémon, tanto na pesquisa individual quanto para carregar a biblioteca
def card_pokemon(poke:dict, sex: bool, size: float, shadow: float, spread: float, offset: list, click: bool, name: bool) -> ft.Container:
    #Cria o sprite do pokémon e o fundo
    if poke['sprite']['front'] == None:
        image = ft.Container(
            expand=3,
            alignment=ft.alignment.top_center,
            border_radius=ft.border_radius.vertical(top=20,bottom=0),
            content= ft.Image(src='https://c.tenor.com/P3RqQUUK9BAAAAAd/tenor.gif', scale=1.5, tooltip='Sem imagem')
        )
    else:
        image = ft.Container(
            expand=3,
            alignment=ft.alignment.top_center,
            border_radius=ft.border_radius.vertical(top=20,bottom=0),
            clip_behavior=ft.ClipBehavior.NONE,
            content= ft.Image(src=poke['sprite']['front'], scale=1.5)
        )
    
    image.gradient = ft.LinearGradient( #Adiciona a cor do primeiro tipo do pokémon ao fundo
        begin=ft.alignment.bottom_left,
        end=ft.alignment.top_right,
        colors=[pt.type_color[poke['type'][0]]]
    )
    #Caso ela tenha um segundo tipo adiciona a cor, caso não, adiciona preto
    image.gradient.colors.append(pt.type_color[poke['type'][1]]) if len(poke['type']) > 1 else image.gradient.colors.append('black')

    #Função que muda o sprite do pokémon, é ativada na interação do botão de sexo
    def change_sex(e):
        if e.data == '1':
            #Verifica se o sprite feminino existe
            if poke['sprite_female']['front']:
                image.content = ft.Image(src= poke['sprite_female']['front'], scale=1.5)
                image.update()
            else:
                return
        else:
            if poke['sprite']['front'] == None:
                return
            image.content.src = poke['sprite']['front']
            image.update()
            
    #Cria o botão pra mudar o sexo do pokémon
    sex_button = ft.Container(
        expand=1,
        alignment=ft.alignment.center,
        bgcolor='black',
        content= ft.CupertinoSlidingSegmentedButton(
            selected_index=0,
            thumb_color='black',
            padding=ft.padding.all(0),
            on_change=change_sex,
            controls=[
                ft.Icon(name=ft.icons.MALE_ROUNDED, color=ft.colors.BLUE),
                ft.Icon(name=ft.icons.FEMALE_ROUNDED, color=ft.colors.PINK)
            ]
        )
    )

    #Cria a parte de baixo do card com os tipos
    info = ft.Container(
        expand=1,
        alignment=ft.alignment.center,
        bgcolor='black',
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=0,bottom=20),
        content=ft.Container(
            content= ft.Row(
                expand=1,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[]
            )
        )
    )
    for i in poke['type']: #Adiciona os tipos dinamicamente
        info.content.content.controls.append(
            ft.Container(
                bgcolor='black',
                padding=ft.padding.all(3),
                border_radius=ft.border_radius.all(7),
                content=ft.Text(value=poke['type'][poke['type'].index(i)].capitalize(), color=pt.type_color[poke['type'][poke['type'].index(i)]])
            )
        )

    #Cria o container do card e adiciona os itens anteriores
    body = ft.Container(
        width=100 * size,
        height=100 * size,
        ink = True,
        bgcolor='transparent',
        clip_behavior=ft.ClipBehavior.NONE,
        shadow=ft.BoxShadow(blur_radius= shadow, color=pt.type_color[poke['type'][0]], spread_radius=spread, offset= ft.Offset(offset[0], offset[1])),
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(20),
        content=ft.Column(
            spacing=0,
            controls=[
                image
            ]
        )
    )
    poke_name = '#' + str(poke['id']) + ' ' + poke['name'].capitalize()
    if name:
        body.content.controls.append(ft.Container(content=ft.Text(value=poke_name, color='white', weight=ft.FontWeight.W_500), width = 500, alignment=ft.alignment.center, bgcolor='black', expand=1))
    body.content.controls.extend([sex_button, info]) if sex else body.content.controls.append(info)
    if click:
        body.on_click = lambda e: poke_body(e, poke['name'])

    return body

#Função para criar a base das páginas de cada aba
def create_layout():
    layout = ft.Container(
            alignment= ft.alignment.center,
            content=ft.Column(
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            )
        )

    return layout