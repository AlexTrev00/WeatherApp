import requests

def temperatura_de_lugar (place):
    parameters = {'key' : 'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place,
                  'units':'metric', 'language': 'es'}
    url = "https://www.meteosource.com/api/v1/free/point"
    data = requests.get(url, parameters).json()
    return f"la temperatura actual de {place} es {data["current"], ["temperature"]} °C"

def clima_lugar_icono (place):
    parameters = {'key': 'rxsjl8vt5wbc5x5twoz149tf8bfnbgzsm1c0vcnb', 'place_id': place,}
    url = "https://www.meteosource.com/api/v1/free/point"
    data = requests.get(url, parameters).json()
    return f"{data["current"],["icon"]}"




if __name__ == "__main__":
    temperatura_de_lugar()
    clima_lugar_icono()