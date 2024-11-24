import requests


def fetch_weather_data(place):
    params = {'lang': 'ru', 'nTqum': ''}
    url = f'http://wttr.in/{place}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        try:
            weather = fetch_weather_data(place)
            print(f'Weather data for {place}:\n{weather}\n')
        except requests.exceptions.RequestException as err:
            print(f'Error occurred while fetching weather for {place}: {err}\n')


if __name__ == "__main__":
    main()
