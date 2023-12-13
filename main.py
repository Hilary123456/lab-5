import tkinter as tk
from PIL import Image, ImageTk
import requests
import json
import io


def get_weather(city):
    api_key = "590260f28e26ef37fbb58452bd15161c"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    print(f"Weather in {city}: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")


def get_movies():
    url = "https://api.kinopoisk.dev/v1.4/movie/500"
    headers = {
        'url': url,
        'accept': 'application/json',
        'X-API-KEY': 'Q2C39YG-JR54JFW-M8JQT2G-78T6FVS',
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    # print(data)

    # Extract 5-7 fields
    field1 = data.get('name')
    field2 = data.get('id')
    field3 = data.get('genres')
    field4 = data.get('isSeries')
    field5 = data.get('year')

    print(f"Name: {field1}, \n id: {field2}, \ngenres: {field3}, \nis Series? {field4}, \nyear: {field5}")

class ImageGenerator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button = tk.Button(self.frame, text="Generate Image", command=self.update_image)
        self.button.pack()

        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        self.update_image()

    def update_image(self):
        response = requests.get('https://randomfox.ca/floof/')
        data = response.json()
        image_url = data['image']

        image_response = requests.get(image_url)
        image_bytes = io.BytesIO(image_response.content)

        self.image = Image.open(image_bytes)
        self.photo_image = ImageTk.PhotoImage(self.image)

        self.image_label.config(image=self.photo_image)

def main():
    print("1. Получить данные из OpenWeather")
    get_weather("Saint Petersburg")

    print("2. Из варианта 7 получение данных с kinopoisk.dev")
    get_movies()

    print("3. допзадание")
    root = tk.Tk()
    app = ImageGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
