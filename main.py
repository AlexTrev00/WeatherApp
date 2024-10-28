import requests
from datetime import datetime


def temperatura_de_lugar (place):
    try:
        parameters = {'key' : 'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place}
        url = "https://www.meteosource.com/api/v1/free/point"
        data = requests.get(url, parameters).json()
        temp = data['current']['temperature']
        return f"{temp} °C"
    except:
        print("Lugar geografico no accesible, intente de nuevo")
def icono_clima(place):
    try:
        parameters = {'key' : 'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place}
        url = "https://www.meteosource.com/api/v1/free/point"
        data = requests.get(url, parameters).json()
        icono = data['current']['icon_num']
        return f"https://www.meteosource.com/static/img/ico/weather/{icono}.svg"
    except :
        return 'imagen no disponible'
    
def time_zone (place):
    params = {'key':'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place,}
    url = "https://www.meteosource.com/api/v1/free/point"
    try:
        data = requests.get(url, params).json()
        data_byhour = data.get("hourly", {}).get("data",[])
        hour_str = data_byhour[0]["date"]
        hour_obj = datetime.fromisoformat(hour_str)
        return hour_obj.strftime("%H:%M")
    except (requests.RequestException, KeyError, IndexError) as error:
        return f"hora no disponible {error}" 

def forecast (place):
    params= {'key':'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place} 
    url = "https://www.meteosource.com/api/v1/free/point"
    data = requests.get(url, params).json()
    wind_speed= data['current']['wind']['speed']
    wind_dir = data['current']['wind']['dir']
    return f'{wind_speed} {wind_dir}'

#if __name__ == "__main__":
 #   print (temperatura_de_lugar('japan'))
  #  print (clima_lugar_icono('japan'))
