import bs4
import requests

url = "http://cecyteq.edu.mx/SGC/CECyTEQ-SGC/OfertaEducativa.html"

pagina = requests.get(url)

html = pagina.content

soup = bs4.BeautifulSoup(html, "lxml")

div_class = "crux-body-copy"

div_tags = soup.find_all("div", class_=div_class)

for tag in div_tags:
    print(tag)
