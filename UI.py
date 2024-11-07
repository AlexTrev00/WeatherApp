import flet as ft
from main import temperatura_de_lugar, time_zone, forecast, icono_clima, name_icono, regex
from excel_functions import guardar_en_excel




class SearchButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor="#002b6e"
        self.color="#ffffff"
        self.on_click=on_click
        self.text = text
        self.icon= ft.icons.SEARCH
class requestStyle ():
    def __init__(self, text):
        super().__init__()
        self.color= '#ffffff'
        self.font_family = 'Noto Sans Japanese'
        self.size = 16
        self.text = text
class excelButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor="#002b6e"
        self.color="#ffffff"
        self.on_click=on_click
        self.text = text

        

def main(page: ft.Page):
    page.window.width=600
    page.window.height=550
    page.bgcolor="#ffffff"
    title_app = ft.Text("Weather App", color="#ffffff")
    time =  ft.Text("", color="#ffd800")
    page.appbar = ft.AppBar(
        # se envuelve todo el text en una fila para poder centrarlo con alignment
        title= ft.Row (             
            controls=[
                title_app,
                time
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#002b6e",
    )
    content_container = ft.Column()
    txt_field = ft.TextField(text_align=ft.TextAlign.CENTER, width=300, height=40, color="#002b6e")
    
    btn_excel = excelButton(text='Excel Report', on_click=lambda e:excel_funcion(e))
    btn_excel.visible = False
    def ok_clicked(e):
        place = txt_field.value
        if place:
            reg = regex(place)
            # condicional de la funcion regex 
            if reg != True:
                secondary_row = ft.Row (
                    controls=[
                        ft.Container(
                            content=ft.Text('Lo Siento, solo se admiten letras, intente de nuevo', color="#ffd800", font_family='Noto Sans Japanese', size=16, weight=ft.FontWeight.BOLD),
                            padding=20,
                            bgcolor='#234b76',
                            border_radius=10,
                            margin=20,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
                content_container.controls.append(secondary_row)
                page.add(content_container)
                page.update()
            
            #txt_field.value = ""
            content_container.controls.clear()

            temperature = temperatura_de_lugar(place)
            icon_url = icono_clima(place)
            timezone = time_zone(place)
            daily_time = forecast(place)
            icon_description = name_icono(place)
            

            time.value= f"{timezone} {place.capitalize()}"
            page.appbar.update()
            

            content_row = ft.Row (
                controls=[
                    ft.Container(
                        content=ft.Text(temperature, color="#ffd800", font_family='Noto Sans Japanese', size=16, weight=ft.FontWeight.BOLD),
                        padding=20,
                        bgcolor='#234b76',
                        border_radius=10,
                        margin=20,
                    ),
                    ft.Container(
                        content= ft.Column (
                            controls = [
                                ft.Image(src=icon_url, width=60, height=60),
                                ft.Text(icon_description, color='#ffd800', font_family='Noto Sans Japanese', size=16, weight=ft.FontWeight.BOLD)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        padding=20,
                        bgcolor='#234b76',
                        border_radius=10,
                        margin=20
                    ),
                    ft.Container(
                        content= ft.Column (
                            controls = [
                                ft.Text('Wind Speed', color='#ffd800', font_family='Noto Sans Japanese', size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(daily_time , color='#ffd800', font_family='Noto Sans Japanese', size=16, weight=ft.FontWeight.BOLD),
                            ],
                        ),
                        padding=20,
                        bgcolor='#234b76',
                        border_radius=10,
                        margin=20,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )     
            #limpia el contenido anterior para mostrar la nueva solicitud 
            content_container.controls.append(content_row)
            btn_excel.visible=True
            btn_excel_row = ft.Row(
                controls=[
                    btn_excel
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            content_container.controls.append(btn_excel_row)
            page.add(content_container)
            page.update()
    def excel_funcion(e):
        place = txt_field.value
        guardar_en_excel(place)
        

    def btn_visibility():
        btn_excel.visible = bool(txt_field.value)
        page.update()
    
    txt_field.on_change = btn_visibility

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
