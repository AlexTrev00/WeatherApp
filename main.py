import requests
from datetime import datetime
import re

'''API_KEY y url para solicitar los datos a la API
API_KEY = 'lkzersr1hytpof1wj54ma832l6nr1wuqshjjx12a'
BASE_URL = "https://www.meteosource.com/api/v1/free/point".

'''
API_KEY = 'lkzersr1hytpof1wj54ma832l6nr1wuqshjjx12a'
BASE_URL = "https://www.meteosource.com/api/v1/free/point"


def regex(place):
    '''Funcion de expresion regular
    exp = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(\s+[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$".'''
    exp = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+(\s+[a-zA-ZáéíóúÁÉÍÓÚñÑ]+)*$"
    matches = re.match(exp, place)
    return matches is not None


def temperatura_de_lugar (place):
    '''Funcion que devuelvele la temperatura del lugar
    try:
        parameters = {'key' : API_KEY, 'place_id': place, 'units':'metric'}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        #temp = data['current']['temperature']
        return f"{data['current']['temperature']} °C"
    except:
        print("Lugar geografico no accesible, intente de nuevo").'''
    try:
        parameters = {'key' : API_KEY, 'place_id': place, 'units':'metric'}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        #temp = data['current']['temperature']
        return f"{data['current']['temperature']} °C"
    except:
        print("Lugar geografico no accesible, intente de nuevo")


def icono_clima(place):
    '''Funcion que devuelve el icono respectivo del estado climatologico del lugar
    try:
        parameters = {'key' : API_KEY, 'place_id': place}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        icono = data['current']['icon_num']
        return f"https://www.meteosource.com/static/img/ico/weather/{icono}.svg"
    except :
        return 'imagen no disponible'.'''
    try:
        parameters = {'key' : API_KEY, 'place_id': place}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        icono = data['current']['icon_num']
        return f"https://www.meteosource.com/static/img/ico/weather/{icono}.svg"
    except :
        return 'imagen no disponible'


def name_icono (place):
    '''Funcion que devuelve el nombre representativo al icono del clima
    try:
        parameters = {'key' : API_KEY, 'place_id': place}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        icon_name = data['current']['summary']
        return f"{icon_name}"
    except :
        return f'no se encuentra el estado actual del clima en {place}'.'''
    try:
        parameters = {'key' : API_KEY, 'place_id': place}
        url = BASE_URL
        data = requests.get(url, parameters).json()
        icon_name = data['current']['summary']
        return f"{icon_name}"
    except :
        return f'no se encuentra el estado actual del clima en {place}'


def time_zone (place):
    '''Funcion que devuelve la zona horaria actual
    params = {'key':API_KEY, 'place_id': place, }
    url = BASE_URL
    try:
        data = requests.get(url, params).json()
        data_byhour = data.get("hourly", {}).get("data",[])
        hour_str = data_byhour[0]["date"]
        hour_obj = datetime.fromisoformat(hour_str)
        return hour_obj.strftime("%H:%M")
    except (requests.RequestException, KeyError, IndexError) as error:
        return f"hora no disponible {error}" .'''
    params = {'key':API_KEY, 'place_id': place, }
    url = BASE_URL
    try:
        data = requests.get(url, params).json()
        data_byhour = data.get("hourly", {}).get("data",[])
        hour_str = data_byhour[0]["date"]
        hour_obj = datetime.fromisoformat(hour_str)
        return hour_obj.strftime("%H:%M")
    except (requests.RequestException, KeyError, IndexError) as error:
        return f"hora no disponible {error}" 


def forecast (place):
    '''Funcion que devuelve la velocidad actual del viento, asi como, la direccion del viento
    params= {'key':API_KEY, 'place_id': place, 'units':'metric'} 
    url = BASE_URL
    data = requests.get(url, params).json()
    wind_speed= data['current']['wind']['speed']
    conv = wind_speed * 3.6 
    wind_dir = data['current']['wind']['dir']
    return f'{conv:.2f}km/h {wind_dir}'.'''
    params= {'key':API_KEY, 'place_id': place, 'units':'metric'} 
    url = BASE_URL
    data = requests.get(url, params).json()
    wind_speed= data['current']['wind']['speed']
    conv = wind_speed * 3.6 
    wind_dir = data['current']['wind']['dir']
    return f'{conv:.2f}km/h {wind_dir}'

'''if __name__ == "__main__":
    temperatura_de_lugar("monterrey")
    time_zone("monterrey")
    forecast("monterrey")
'''
