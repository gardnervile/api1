import requests
import logging


def configure_logging():
    logging.basicConfig(level=logging.DEBUG)


def fetch_weather_data():
    params = {'lang': 'ru', 'nTqum': ''}
    url_template = 'http://wttr.in/{}'
    places = ['Лондон', 'Шереметьево', 'Череповец']

    for place in places:
        try:
            url = url_template.format(place)
            response = requests.get(url, params=params)
            logging.debug(response.url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f'Error occurred: {err}')
        else:
            logging.debug(response.text)


def main():
    configure_logging()
    fetch_weather_data()


if __name__ == "__main__":
    main()
