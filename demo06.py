from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import re

# 爬取豆瓣电影 Top 250

head = {}
head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"

url = "https://movie.douban.com/top250?start={}&filter="

Filmlist = []

def getFilm(url):
	req = Request(url, None, head)
	html = urlopen(req)
	bs = BeautifulSoup(html.read(), 'html.parser')
	filmList = bs.find_all('div', {'class': 'info'})
	if len(filmList) == 0:
		return False
	for film in filmList:
		filmName = film.div.a.span
		# print(filmName.get_text())
		Filmlist.append(filmName.get_text())
	return True



def main():
	num = '0'
	newurl = url.format(num)
	while getFilm(newurl):
		num = str(int(num) + 25)
		newurl = url.format(num)

	for i in range(len(Filmlist)):
		print("{}: {}".format(i + 1, Filmlist[i]))

if __name__ == '__main__':
	main()