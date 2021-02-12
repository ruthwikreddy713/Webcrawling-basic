from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
imdb1to50="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
imdb50to100="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt"
top50=req(imdb1to50)
top50page= soup(top50.read(),"html.parser")
top50.close()
top100=req(imdb50to100)
top100page=soup(top100.read(),"html.parser")
top100.close()
top50arr=top50page.findAll("div", {"class":"lister-item mode-advanced"})
top100arr=top100page.findAll("div",{"class": "lister-item mode-advanced"})
#print(top50arr)
opfile="imdbtop100.csv"
headers="Sno,Title,year,rating,votes \n"
f=open(opfile,"w")
f.write(headers)
#print(top100arr[49].h3.a.text)
#sno=top50arr[0].find("span", {"class": "lister-item-index unbold text-primary"}).text.replace(".","")
#print(sno)
#year = top50arr[0].find("span",{"class": "lister-item-year"}).text[1:5]
#rating=top50arr[0].strong.text
#votes=top50arr[0].find("span",{"name":"nv"}).text
#print(votes)
#print(rating)
#print(year)
for movie in top50arr:
	Sno= movie.find("span", {"class": "lister-item-index unbold text-primary"}).text.replace(".","")
	Title=movie.h3.a.text
	Year = movie.find("span",{"class": "lister-item-year"}).text[1:5]
	rating=movie.strong.text
	votes=movie.find("span",{"name":"nv"}).text.replace(",","")
	f.write(Sno + ", "+ Title.replace(",", "|") + ", " + Year + ", " + rating + ", " + votes + "\n")
	print(Sno + ' ' + Title + ' ' + Year + ' ' + rating + ' ' + votes)
for movie in top100arr:
	Sno= movie.find("span", {"class": "lister-item-index unbold text-primary"}).text.replace(".","")
	Title=movie.h3.a.text
	Year = movie.find("span",{"class": "lister-item-year"}).text[1:5]
	rating=movie.strong.text
	votes=movie.find("span",{"name":"nv"}).text.replace(",","")
	f.write(Sno + ", "+ Title.replace(",", "|") + ", " + Year + ", " + rating + ", " + votes + "\n")	
	print(Sno + ' ' + Title + ' ' + Year + ' ' + rating + ' ' + votes)
