import requests


def fetch_weather_data(place):
    params = {'lang': 'ru', 'nTqum': ''}
    url = f'http://wttr.in/{place}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def get_weather_safely(place):
    try:
        return fetch_weather_data(place)
    except requests.exceptions.RequestException as err:
        return f'Error occurred while fetching weather for {place}: {err}'


def main():
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        print(f'Weather data for {place}:\n{get_weather_safely(place)}\n')


if __name__ == "__main__":
    main()
