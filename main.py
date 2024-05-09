import requests
import flet as ft
import patterns as pt
import components as comp

api = "https://pokeapi.co/api/v2/"
poke = "pokemon/"
contador = 0


def main(page: ft.Page):
  page.title = "teste v0.1"
  page.bgcolor = 'black'
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

  def teste_poke(e):
    search_value = e.control.value
    if len(page.controls[-1].controls) > 1:
      del(page.controls[-1].controls[-1])
    pokemon = requests.get(api + poke + search_value).json()
    sprites = {
      'front': pokemon['sprites']['front_default'],
      'back': pokemon['sprites']['back_default'],
      'front_shiny': pokemon['sprites']['front_shiny'],
      'back_shiny': pokemon['sprites']['back_shiny'],
    }

    sprites_img = ft.Column(
      controls=[
        ft.Row(
          controls=[
            ft.Image(src=sprites['front']),
            ft.Image(src=sprites['front_shiny'])
          ],
          alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
          controls=[
            ft.Image(src=sprites['back']),
            ft.Image(src=sprites['back_shiny'])
          ],
          alignment= ft.MainAxisAlignment.CENTER
        )
      ]
    )

    page.controls[-1].controls.append(sprites_img)
    page.update()
    

  def change_tab(e):
    main_index = e.control.selected_index

    if main_index == 0:
      search_poke = comp.search_bar(teste_poke, ft.MainAxisAlignment.CENTER)
      if len(page.controls) > 1:
        del(page.controls[-1])
        page.update()
      layout = ft.Column()
      page.add(layout)
      page.controls[-1].controls.append(search_poke)
      page.update()

    if main_index == 1:
      if len(page.controls) > 1:
        del(page.controls[-1])
        page.update()

    if main_index == 2:
      if len(page.controls) > 1:
        del(page.controls[-1])
        page.update()

  nav_bar = comp.create_nav_bar(change_tab)

  page.add(nav_bar)

ft.app(target=main)