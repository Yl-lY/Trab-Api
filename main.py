import requests
import flet as ft

def main(page: ft.Page) -> None:
    #configuração do layout da página
    page.title = "Pokémon"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # api_poke = "https://pokeapi.co/api/v2/pokemon/"
    # pokemon = requests.get(api_poke + str(texto.value))

    def pesq_poke():
        pass

    texto = ft.TextField(label="Pesquisar", on_submit=pesq_poke)
    button_pesq = ft.ElevatedButton(text="Pesquisar", on_click=pesq_poke, icon="search_rounded", height=50)

    layout = ft.Container(
        margin = ft.margin.all(20),
        content= ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            height=100,
            controls=[
                texto,
                button_pesq
            ]
        )
        
    )

    page.add(layout)
    #teste

ft.app(target=main)