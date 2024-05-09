import flet as ft

navigation_icon_pokemon = ft.Icon(name=ft.icons.CATCHING_POKEMON)
navigation_icon_pokemon_activated = ft.Icon(name=ft.icons.CATCHING_POKEMON, color='red')
navigation_icon_pokedex = ft.Icon(name=ft.icons.LIBRARY_BOOKS_OUTLINED)
navigation_icon_pokedex_activated = ft.Icon(name=ft.icons.LIBRARY_BOOKS_OUTLINED, color='blue')
navigation_icon_moves = ft.Icon(name=ft.icons.BOLT)
navigation_icon_moves_activated = ft.Icon(name=ft.icons.BOLT, color='yellow')

type_color = {
    'bug': '#9ACD32',
    'plant': '#7CFC00',
    'normal': '#8FBC8B',
    'psychic': '#FFC0CB',
    'ghost': '#663399',
    'ground': '#DAA520',
    'metal': '#D3D3D3',
    'ice': '#ADD8E6',
    'rock': '#BC8F8F',
    'dark': '#2F4F4F',
    'water': '#00BFFF',
    'fighting': '#DC143C',
    'poison': '#BA55D3',
    'electric': '#FFFF00',
    'dragon': '#0000CD',
    'flying': '#E0FFFF',
    'fire': '#FF8C00',
    'fairy': '#FF69B4'
}