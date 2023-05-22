import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("Empire's 100 Greatest Movies of All Time.txt", mode="w", encoding="utf8") as file:
    file.write("The 100 Greatest Movies \n")
    file.write("Source: Empire Online\n")
    file.write(
        "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/\n\n")
    for movie in movies:
        file.write(f"{movie}\n")

    print("Successfully written to file.")
