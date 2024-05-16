import flet as ft
import patterns as pt

def create_nav_bar(func_name):
    navigation_bar = ft.NavigationBar(
        destinations=[
        ft.NavigationDestination(icon_content=pt.navigation_icon_pokemon, selected_icon_content=pt.navigation_icon_pokemon_activated, label='Pokémon'),
        ft.NavigationDestination(icon_content=pt.navigation_icon_pokedex, selected_icon_content=pt.navigation_icon_pokedex_activated, label='Pokédex'),
        ft.NavigationDestination(icon_content=pt.navigation_icon_moves, selected_icon_content=pt.navigation_icon_moves_activated, label='moves')
        ],
        on_change= func_name,
        selected_index=1
    )
    return navigation_bar

def search_bar(func_name, align = ft.MainAxisAlignment.START):
    search_bar = ft.Row(
        controls=[
            ft.TextField(label='Pokémon', on_submit=func_name),
            ft.ElevatedButton(content=ft.Icon(name=ft.icons.SEARCH_ROUNDED), on_click=func_name)
        ],
        alignment= align
    )
    return search_bar

def card_pokemon(poke:dict, sex: bool, size: float, shadow: float) -> ft.Container:
    image = ft.Container(
        expand=3,
        alignment=ft.alignment.top_center,
        border_radius=ft.border_radius.vertical(top=20,bottom=0),
        clip_behavior=ft.ClipBehavior.NONE,
        content= ft.Image(src=poke['sprite']['front'], scale=1.5)
    )
    
    image.gradient = ft.LinearGradient(
        begin=ft.alignment.bottom_left,
        end=ft.alignment.top_right,
        colors=[pt.type_color[poke['type'][0]]]
    )

    image.gradient.colors.append(pt.type_color[poke['type'][1]]) if len(poke['type']) > 1 else image.gradient.colors.append('black')

    def change_sex(e):
        if e.data == '1':
            if poke['sprite_female']['front']:
                image.content = ft.Image(src= poke['sprite_female']['front'], scale=1.5)
                image.update()
            else:
                ft.alert.dialog()
        else:
            image.content.src = poke['sprite']['front']
            image.update()
            

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
    for i in poke['type']:
        info.content.content.controls.append(
            ft.Container(
                bgcolor='black',
                padding=ft.padding.all(3),
                border_radius=ft.border_radius.all(7),
                content=ft.Text(value=poke['type'][poke['type'].index(i)].capitalize(), color=pt.type_color[poke['type'][poke['type'].index(i)]])
            )
        )

    body = ft.Container(
        width=100 * size,
        height=100 * size,
        bgcolor='transparent',
        clip_behavior=ft.ClipBehavior.NONE,
        shadow=ft.BoxShadow(blur_radius= shadow, color=pt.type_color[poke['type'][0]]),
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(30),
        content=ft.Column(
            spacing=0,
            controls=[
                image
            ]
        )
    )

    body.content.controls.extend([sex_button, info]) if sex else body.content.controls.append(info) 

    return body


def create_layout():
    layout = ft.Container(
            alignment= ft.alignment.center,
            content=ft.Column(
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
            )
        )

    return layout