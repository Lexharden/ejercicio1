import json
import requests

url = 'https://api.datos.gob.mx/v1/calidadAire'
lista = []
if __name__ == '__main__':
    data = requests.get(url)
    if data.status_code == 200:
        res = json.loads(data.text)
        for i in res['results']:
            if i['_id'] == '58c780bf281e87010078f491':
                measu = i['stations']
                for i in measu:
                    data1 = (i['measurements'])
                    print(data1)

                # lista.append(dic)
                print(measu)
        # print(lista)
