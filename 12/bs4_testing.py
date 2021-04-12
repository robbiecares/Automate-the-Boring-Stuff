import bs4
import lxml
import requests

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml')
# print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'lxml')
# print(type(exampleSoup))

elems = exampleSoup.select('button[value="favorite"]')

print(type(elems))

print(len(elems))

print(type(elems[0]))

print(str(elems[0]))

# print(str(elems[1]))

print(elems[0].getText())

print(elems[0].attrs)
