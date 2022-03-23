import requests


def weather(place):
    url = f'https://wttr.in/{place}?nTqm&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['London', 'SVO', 'Череповец']
    for place in places:
        print(weather(place))
