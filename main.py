import requests
from bs4 import BeautifulSoup

url = "https://www.seek.co.nz/react-jobs/in-auckland"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.get_text()