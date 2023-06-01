import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

def get_weather():
    url = "https://ua.sinoptik.ua/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    temperature_element = soup.find(class_="today-temp")
    temperature = temperature_element.get_text(strip=True) if temperature_element else "Нет данных"

    return temperature

def insert_weather_data(date, time, temperature):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS weather_data
                 (date text, time text, temperature text)''')

    c.execute("INSERT INTO weather_data VALUES (?, ?, ?)", (date, time, temperature))

    conn.commit()
    conn.close()

current_date = datetime.date.today().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

temperature = get_weather()

insert_weather_data(current_date, current_time, temperature)

print("Дата:", current_date)
print("Время:", current_time)
print("Температура:", temperature)
