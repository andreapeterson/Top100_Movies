from bs4 import BeautifulSoup
import requests

### SET- UP
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

### WEBSCRAPING + FORMATING MOVIES LIST
movies_formatted = [movie.text for movie in soup.find_all(name="h3", class_="title")]

movies_inorder = movies_formatted[::-1]

### LIST INTO .TXT FILE
with open("top100_movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_inorder:
        file.write(movie + "\n")
