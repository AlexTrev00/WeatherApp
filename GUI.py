import flet as ft
from main import temperatura_de_lugar, clima_lugar_icono


class SearchButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor="#002b6e"
        self.color="#ffffff"
        self.on_click=on_click
        self.text = text
        self.icon= ft.icons.SEARCH


def main(page: ft.Page):
    page.bgcolor="#ffffff"
    page.appbar = ft.AppBar(
        # se envuelve todo el text en una fila para poder centrarlo con alignment
        title= ft.Row (             
            controls=[
                ft.Text("Weather App", color="#ffffff"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#002b6e",
    )
    txt_field = ft.TextField(text_align=ft.TextAlign.LEFT, width=300, height=40, color="#002b6e")
    def ok_clicked(e):
        place = txt_field.value
        if place:
            temperature = temperatura_de_lugar(place)
            icon_weather= clima_lugar_icono(place)

            page.add (
                ft.Row (
                controls = [
                   ft.Text(temperature, color="#002b6e"),
                  ft.Image(icon_weather)
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
             ),

    page.add(
        ft.Row (
            [
                SearchButton(text='Search',on_click=ok_clicked),
                txt_field
            ],
            alignment=ft.MainAxisAlignment.CENTER
            

        )
        
    )


ft.app(main)
