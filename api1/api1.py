import requests


params = {'lang': 'ru', 'nTqum': ''}
url_template = 'http://wttr.in/{}'
places = ['Лондон', 'Шереметьево', 'Череповец']

for place in places:
    url = url_template.format(place)
    response = requests.get(url, params=params)
    print(response.url)
    print(response.text)
