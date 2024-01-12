import flet as ft

def main(page: ft.Page):
    page.title = "Personal Finance"
    page.scroll = "Olá Andy" 

    t = ft.Text()
    tb = ft.TextField(
        label="R$",
        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
        
    )

    page.add(
        ft.Text("Olá Andy!", style=ft.TextThemeStyle.HEADLINE_LARGE),
        
        ft.Text("Digite o valor da sua renda nesse mês:", style=ft.TextThemeStyle.TITLE_LARGE),
    )
    
    page.add(tb,t)
    
    contas_text = ft.Text()
    lazer_text = ft.Text()
    invest_text = ft.Text()
    
    page.add(
        ft.Text("Contas: ", style=ft.TextThemeStyle.BODY_LARGE),
        contas_text,
        
        ft.Text("Lazer: ", style=ft.TextThemeStyle.BODY_LARGE),
        lazer_text,
        
        ft.Text("Investimentos: ", style=ft.TextThemeStyle.BODY_LARGE),
        invest_text,
    )
    
ft.app(target=main)