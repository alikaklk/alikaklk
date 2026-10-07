import requests
from bs4 import BeautifulSoup
import json

url = "https://github.com/users/alikaklk/contributions"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    days = []
    for day in soup.find_all('td', class_='ContributionCalendar-day'):
        date = day.get('data-date')
        level = day.get('data-level')
        if date:
            days.append({"date": date, "level": int(level) if level else 0})
    
    with open("data/contributions.json", "w") as f:
        json.dump(days, f)
    print("Katkı verileri başarıyla çekildi ve kaydedildi.")
else:
    print("Veri çekilemedi, durum kodu:", response.status_code)
