import flet as ft

def main(page: ft.Page):
    # Número total de elementos
    total_items = 1000

    # Tamanho da janela de carregamento de itens (ajuste conforme necessário)
    window_size = 50
    
    # Container principal com scroll
    scroll_container = ft.Container(
        content=ft.Column(scroll="auto"),
        width=page.window_width,
        height=page.window_height
    )

    # Lista para armazenar os itens
    items = []

    def load_items(offset):
        for i in range(offset, min(offset + window_size, total_items)):
            item = ft.Container(
                content=ft.Row(
                    controls=[ft.Text(f"Item {i}")],
                    wrap=True
                ),
                height=50
            )
            items.append(item)
        scroll_container.content.controls = items
        page.update()

    def on_scroll(e):
        scroll_offset = e.control.scroll_offset
        new_offset = int(scroll_offset / 50)  # 50 is the height of each item
        if len(items) < total_items:
            load_items(new_offset)
        page.update()

    # Inicializa com os primeiros itens visíveis
    load_items(0)

    # Adiciona o listener de scroll
    scroll_container.content.on_scroll = on_scroll

    # Adiciona o container na página
    page.add(scroll_container)

ft.app(target=main)