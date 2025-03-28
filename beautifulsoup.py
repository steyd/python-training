from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())

# print(soup.find_all('img')) -- [<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]

image1, image2 = soup.find_all('img')
print(image1.name)
print(image1["src"])
print(image2["src"])

# print(soup.title) -- <title>Profile: Dionysus</title>
print(soup.title.string)