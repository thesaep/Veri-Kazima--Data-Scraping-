from bs4 import BeautifulSoup
import requests

film=0

r = requests.get("https://www.imdb.com/chart/top")
imdb = BeautifulSoup(r.content,"html.parser")

findname = imdb.find("table",{"class":"chart full-width"}).find("tbody").find_all("tr")


for film in findname:
    if float(film.find("td",{"class":"ratingColumn imdbRating"}).text) >= 8.5:
        print(film.find("td",{"class":"titleColumn"}).text.replace("\n",""),end='\t\t')
        print(film.find("td",{"class":"ratingColumn imdbRating"}).text.replace("\n",""))
        
