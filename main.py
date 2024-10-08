import flet as ft
import components as comp
import functions as func

def main(page: ft.Page):
  page.title = "PokéFlet"
  page.bgcolor = 'black'
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.theme_mode = ft.ThemeMode.DARK
  page.window_min_height, page.window_height = [600, 600]
  page.window_min_width, page.window_width = [1000, 1000]
  #Tudo isso pra cima são ajustes na tela
  dex = []
  #Função para carregar os pokémon pesquisados na search_bar
  def load_poke(e):
    try:
      search_value = e.control.value
    except AttributeError:
      search_value = page.controls[1].content.controls[0].controls[0].value
    print(search_value)
    if len(page.controls[1].content.controls) > 1:
      del(page.controls[1].content.controls[-1])

    response = func.get_poke(search_value.lower())
    card = comp.card_pokemon(response, True, 1.8, 50, 0, [0, 0], True, False)

    page.controls[1].content.controls.append(card)
    page.update()

  #Função ativada quando trocamos de aba na navigation_bar
  def change_tab(e):
    main_index = e.control.selected_index #Recolhe os dados da navigation_bar

    if main_index == 0:
      search_poke = comp.search_bar(load_poke, ft.MainAxisAlignment.CENTER)

      #Processo básico pra limpar a tela e carregar a nova
      page.controls[1].content.controls.clear()
      page.controls[1].content.controls.append(search_poke)
      page.update()

    
    if main_index == 1:
      page.controls[1].content.controls.clear()
      page.controls[1].padding = ft.padding.all(0) #Só frufru pra formatar quando tiver na pokédex
      page.scroll = ft.ScrollMode.AUTO #Permite o scroll na tela

      chain = ft.Row( #Cria a linha que vamos quebrar, aqui vamos inserir todos os pokémon
          wrap=True,
          width=830,
          spacing=10
        )
      
      def load_chain(pokedex):
        chain.controls.clear()
        for i in pokedex: #Por cada item retornado das 1000 requisições ele cria um card e joga na tela
          # print(i)
          response = func.format_poke(i)
          card = comp.card_pokemon(response, False, 1.3, 1, 1, [-1.5, -1.5], True, True)
          chain.controls.append(card)
          page.controls[1].content.controls[0].controls[3].value = '#' + str(len(page.controls[1].content.controls[1].controls)) + '\nPokémon'
        page.update()

      page.controls[1].content.controls.extend([comp.filter_bar(dex, load_chain), chain]) #Aqui estou adicionando os componentes base da página
      page.update()
      
      page.update() #Só atualiza a tela depois de adicionar todos

    if main_index == 2: #Aqui ainda não tem nada
      page.controls[1].content.controls.clear()
      page.controls[1].content.controls.append(
        ft.Container(
          content= ft.Image(src='https://c.tenor.com/1l9R9y3_WIkAAAAC/tenor.gif'),
          bgcolor='white', width = 1000, height= 600
        )
      )
      page.update()

  page.add(
    ft.Container(
      content= ft.Row(
        alignment= ft.MainAxisAlignment.END,
        vertical_alignment= ft.CrossAxisAlignment.END,
        controls= [ft.Image(
          src='https://media.tenor.com/e6J4X97EZkIAAAAi/ash-now.gif', 
          width=500, 
          height=500)]
      ), expand=True, image_src = 'https://c.tenor.com/iBo9HVsyKjwAAAAC/tenor.gif', image_fit= ft.ImageFit.COVER, alignment= ft.alignment.Alignment(0.0, 6.0)
    )
  )
  dex = func.get_pokedex(False)
  page.controls.clear()

  nav_bar = comp.create_nav_bar(change_tab) #Como python é interpretado, temos que carregar todas essas funções antes de carregar a tela
  layout = comp.create_layout() 



  page.add(nav_bar, layout) #Aqui estamos adicionando os elementos à tela


ft.app(target=main, assets_dir='assets')                        # Esse código faz o Flet rodar como um programa
# ft.app(target=main, assets_dir='assets', view=ft.WEB_BROWSER) # Esse código faz o Flet rodar como um site