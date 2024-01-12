import flet as ft

def main(page: ft.Page):
    page.title = "Personal Finance"
    page.scroll = "Olá Andy"    
    
def main(page: ft.Page):
    def textbox_changed(e):
        t.value = e.control.value
        page.update()

    t = ft.Text()
    tb = ft.TextField(
        label="R$",
        on_change=textbox_changed,
    )

    page.add(
        ft.Text("Olá Andy!", style=ft.TextThemeStyle.HEADLINE_LARGE),
        
        ft.Text("Digite o valor da sua renda nesse mês:", style=ft.TextThemeStyle.TITLE_LARGE),
    )
    
    page.add(tb,t)
    

ft.app(target=main)