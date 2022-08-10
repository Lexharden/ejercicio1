import json
import pprint

import requests

url = 'https://api.datos.gob.mx/v1/calidadAire'
lista = []
if __name__ == '__main__':
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
