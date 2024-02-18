import requests


def SendRequest(link, amount):
    for i in range(amount):
        responce = requests.get(link)

        if responce.status_code != 200:
            return 0
        else:
            requests.get("https://www.youtube.com/")

    return 1
