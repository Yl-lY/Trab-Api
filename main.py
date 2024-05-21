import flet as ft
import patterns as pt
import components as comp
import functions as func
import time

def main(page: ft.Page):
  page.title = "teste v0.1"
  page.bgcolor = 'black'
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.theme_mode = ft.ThemeMode.DARK
  page.window_min_height, page.window_height = [600, 600]
  page.window_min_width, page.window_width = [1000, 1000]


  def load_poke(e):
    try:
      search_value = e.control.value
    except AttributeError:
      search_value = page.controls[1].content.controls.controls[0].value
    print(search_value)
    if len(page.controls[1].content.controls) > 1:
      del(page.controls[1].content.controls[-1])

    response = func.get_poke(search_value)
    card = comp.card_pokemon(response, True, 1.8, 50, 0, [0, 0], True)

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
      page.controls[1].content.controls.clear()
      page.controls[1].padding = ft.padding.all(0)
      page.scroll = ft.ScrollMode.AUTO

      chain = ft.Row(
        wrap=True,
        width=830,
        spacing=10
      )
      page.controls[1].content.controls.extend([comp.filter_bar(), chain])
      page.update()
      start = time.time()
      dex = func.get_pokedex()
      end = time.time()
      print(end - start)
      for i in dex:
        response = func.format_poke(i)
        card = comp.card_pokemon(response, False, 1.3, 1, 1, [-1.5, -1.5], True)
        chain.controls.append(card)
      page.update()

    if main_index == 2:
      page.controls[1].content.controls.clear()
      page.update()


  nav_bar = comp.create_nav_bar(change_tab)
  layout = comp.create_layout()

  page.add(nav_bar, layout)


ft.app(target=main, assets_dir='assets')