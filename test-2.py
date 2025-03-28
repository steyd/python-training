from urllib.request import urlopen
import re # adding re library

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode('utf-8')
start_index = html.find('<title>') + len('<title>')
end_index = html.find('</title>')

title = html[start_index : end_index]
title = re.sub("<.*?>", "", title)
title = re.sub("\n", "", title)

print(title)