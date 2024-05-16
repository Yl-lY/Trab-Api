import requests
import flet as ft
import patterns as pt
import components as comp
import functions as func

api = "https://pokeapi.co/api/v2/"
poke = "pokemon/"
contador = 0


def main(page: ft.Page):
  page.title = "teste v0.1"
  page.bgcolor = 'black'
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


  def load_poke(e):
    try:
      search_value = e.control.value
    except AttributeError:
      search_value = page.controls[1].content.controls.controls[0].value
    print(search_value)
    if len(page.controls[1].content.controls) > 1:
      del(page.controls[1].content.controls[-1])

    response = func.get_poke(search_value)
    card = comp.card_pokemon(response, True, 1.8, 100)

    page.controls[1].content.controls.append(card)
    page.update()
    

  def change_tab(e):
    main_index = e.control.selected_index

    if main_index == 0:
      search_poke = comp.search_bar(load_poke, ft.MainAxisAlignment.CENTER)

      page.controls[1].content.controls.clear()
      page.controls[1].content.controls.append(search_poke)
      page.update()

    if main_index == 1:
      page.scroll = ft.ScrollMode.AUTO

      page.controls[1].content.controls.clear()
      page.update()
      page.controls[1].padding = ft.padding.only(top=0)

      chain = ft.Row(
        wrap=True,
        width=page.window_width * 0.7,
        spacing=10
      )
      page.controls[1].content.controls.append(chain)
      for i in range (30):
        print(i)
        response = func.get_poke(str(i + 1))
        card = comp.card_pokemon(response, False, 1.3, 100)
        chain.controls.append(card)
        cont = i+1
        if cont % 3 == 0:
          page.update()

    if main_index == 2:
      page.controls[1].content.controls.clear()
      page.update()


  nav_bar = comp.create_nav_bar(change_tab)
  layout = comp.create_layout()

  page.add(nav_bar, layout)


ft.app(target=main, assets_dir='assets')