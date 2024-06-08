import flet as ft
from funções import label_text

def main(page: ft.Page):
    page.title = "Minha Calculadora Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def diminuir(e):
        pass  # Implemente a lógica para diminuir aqui

    def somar(e):
        pass  # Implemente a lógica para somar aqui
    btn_diminuir = ft.FilledButton(text="Diminuir", on_click=diminuir)
    btn_somar = ft.FilledButton(text="Somar", on_click=somar)

    page.add(
        btn_diminuir,
        btn_somar,
        label_text(text="olá como vc esta?")
        )
    page.update()
if __name__ == "__main__":
    ft.app(port=8000,target=main)
