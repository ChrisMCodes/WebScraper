import requests
from bs4 import BeautifulSoup

URL = "https://www.upwork.com/search/jobs/?q=Web%20scraping"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("a", class_="job-title-link break visited")

for result in results:
    print(result.get("href"))

