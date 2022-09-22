import requests

peticion = requests.get("https://www.google.com")
print(peticion.status_code)
print(peticion.url)
print(peticion.request)
