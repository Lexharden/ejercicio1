import json
import pprint

import requests


def api_response():
    url = 'https://api.datos.gob.mx/v1/calidadAire'
    lista = []
    data = requests.get(url)
    if data.status_code == 200:
        # pprint.pprint(data.json().get('results'))
        data = data.json().get('results')
        for i in data:
            if i['_id'] == '58c780bf281e87010078f491':
                station = i['stations']
                for e in station:
                    mesau = e['measurements']
                    for j in mesau:
                        value = j['value'], j['unit'], j['pollutant']
                        lista.append(value)
                        print(f'El valor de: 58c780bf281e87010078f491 es:', lista)
                        return j['pollutant']


def encontrar_valor(populant):
    url = 'https://api.datos.gob.mx/v1/calidadAire'
    lista = []
    data = requests.get(url)
    data = data.json().get('results')
    ultimo = data[-1]['stations']
    for e in ultimo:
        mesau = e['measurements']
        for j in mesau:
            value = j['value'], j['unit'], j['pollutant']
            new_valor = populant
            print(value, new_valor)


value_popullant = api_response()
encontrar_valor(value_popullant)
