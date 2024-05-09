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
            ft.ElevatedButton(text='Pesquisar', on_click=func_name)
        ],
        alignment= align
    )
    return search_bar