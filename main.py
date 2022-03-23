import requests


def get_weather(place):
    payload = {'n': '', 'T': '', 'q': '', 'm': '', 'lang': 'ru'}
    url = f'https://wttr.in/{place}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['London', 'SVO', 'Череповец']
    for place in places:
        print(get_weather(place))
