import flet as ft
from main import temperatura_de_lugar, time_zone, forecast, icono_clima, name_icono, regex
from excel_functions import guardar_en_excel

'''Interfaz Grafica de la aplicaion que reune ciertos datos del clima solicitados por el usuario.'''

'''Se define la clase SearchButton con estilos personalizados.'''
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
'''Se define la clase excelButton, esta clase es el estilo del boton Excel Report'''
class excelButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor="#002b6e"
        self.color="#ffffff"
        self.on_click=on_click
        self.text = text

        
'''Se inicia la app.''' 
def main(page: ft.Page):
    '''Se define ancho y alto de la app al abrirse
    page.window.width=600
    page.window.height=550.'''
    page.window.width=600
    page.window.height=550
    '''Se define el color de fondo de la app 
    page.bgcolor="#ffffff".'''
    page.bgcolor="#ffffff"
    '''Titulo de la app
    title_app = ft.Text("Weather App", color="#ffffff").''' 
    title_app = ft.Text("Weather App", color="#ffffff")
    '''Con esta linea definimos que en cuanto se haga una consulta se muestre la hora de color amarillo.'''
    time =  ft.Text("", color="#ffd800")
    '''Definimos un appbar para la aplicacion''' 
    page.appbar = ft.AppBar(
        title= ft.Row (             
            controls=[
                title_app,
                time
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#002b6e",
    )
    '''Definimos esta variable que contiene una estructura de columna vacia para usarla cuando haya alguna error.'''
    content_container = ft.Column()
    '''Txt_field es el campo de texto donde el usuario ingresara su consulta.'''
    txt_field = ft.TextField(text_align=ft.TextAlign.CENTER, width=300, height=40, color="#002b6e")

    '''En esta linea definimos una variable que contiene una clase de estilos definida anteriormente, 
    que contiene una funcion lambda que interactua a la escucha de la funcion excel_funcion
    btn_excel = excelButton(text='Excel Report', on_click=lambda e:excel_funcion(e)).'''
    btn_excel = excelButton(text='Excel Report', on_click=lambda e:excel_funcion(e))
    '''Definimos btn_excel.visible como False, ya que esta es la variable de control que definira si el boton
    de excel report cuando se mostrara el boton excel report
    btn_excel.visible = False.'''
    btn_excel.visible = False
    def ok_clicked(e):
        '''Aqui place es nuestra variable que toma el lugar del valor solicita por el usuario.'''
        place = txt_field.value
        '''Aqui definimos si place tiene un valor'''
        if place:
            '''regex es una funcion de expresion regular que valida el dato ingresado y regresa un booleano.'''
            reg = regex(place)
            '''Condicional de la funcion regex.''' 
            if reg != True:
                '''Si reg es diferente de True muestra secondary row
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
                ).''' 
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
                '''Aqui controlamos que la pantalla se actualize conforme el usuario ingrese datos.'''
                content_container.controls.append(secondary_row)
                page.add(content_container)
                page.update()
            
            #txt_field.value = ""
            content_container.controls.clear()
            '''Si el valor pasa la verificacion regex entonces empiezas a consultar los datos de salida en la API.'''
            temperature = temperatura_de_lugar(place)
            icon_url = icono_clima(place)
            timezone = time_zone(place)
            daily_time = forecast(place)
            icon_description = name_icono(place)
            

            time.value= f"{timezone} {place.capitalize()}"
            page.appbar.update()
            
            '''Los datos se muestran en forma de filas acomodandose en columnas responsivas.'''
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
            '''Limpia el contenido anterior para mostrar la nueva solicitud.'''
            content_container.controls.append(content_row)
            '''Aca se reedefine btn_excel.visible como True ya que este bloque del codigo se ejecuta unicamente cuando
            la busqueda ingresada por el usuario es valida y place ya tomo lugar como string.'''
            btn_excel.visible=True
            '''Se establece la posicion que tomara el boton Excel Report en la aplicacion.'''
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
        '''Se establece que cuando se de click en el boton excel report este mandara a invocar la funcion guardar_en_excel().'''
        place = txt_field.value
        guardar_en_excel(place)
        
    def btn_visibility():
        '''Esta funcion define que cuando btn_excel.visible sea igual a True entonces el boton se mostrara en la aplicacion
        y no se mostrara en caso contrario.'''
        btn_excel.visible = bool(txt_field.value)
        page.update()
    '''Se indica que la funcion btn_visibility() cambiara respecto al cambio de valor en el campo de texto'''
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
