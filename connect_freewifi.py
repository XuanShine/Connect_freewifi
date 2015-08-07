#!/usr/bin/env python3

try:
    from requests import get
    from requests.exceptions import ConnectionError
    from requests.exceptions import SSLError
except ImportError:
    from urllib.request import urlopen as get
    from urllib.parse import urlencode
    from urllib.error import URLError as ConnectionError
    SSLError = ConnectionError
    lib_requests = False
    print("No lib requests, but the script will continue..")
else:
    lib_requests = True

post = {"login": "",
        "password": "",
        "submit": "Valider",
        }

if not lib_requests:  # Post from requests is different than post from urllib
    post = [(key, post[key]) for key in post]

url = "https://wifi.free.fr/Auth"


def authentification(n=1):
    if not lib_requests:
        url_enc = urlencode(post).encode()
        req = get(url, data=url_enc)
        text = req.readline().decode()
    else:
        req = get(url, params=post, verify=False)
        text = req.text

    try:
        assert "CONNEXION AU SERVICE REUSSIE" in text
    except AssertionError:
        print(text)

    if "free" in get("http://google.fr").url:
        print("Connection réussie mais toujours redirigée. Essai:", n)
        authentification(n+1)
    else:
        print("Connection au service réussie")

if __name__ == "__main__":
    if "free" in get("http://google.fr").url:
        authentification(1)
    else:
        print("Vous êtes déjà connecté au réseau")
