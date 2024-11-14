import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "2ac4055ae8412e499a5c604412163953"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_conditions = data["weather"][0]["description"]

            result_label.config(
                text=f"Weather in {city}:\n"
                     f"Temperature: {temperature}°C\n"
                     f"Humidity: {humidity}%\n"
                     f"Conditions: {weather_conditions.capitalize()}"
            )
        else:
            result_label.config(text=f"Error: {data['message']}")

    except requests.ConnectionError:
        result_label.config(text="Network error. Please check your internet connection.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

window = tk.Tk()
window.title("Weather App")

city_label = tk.Label(window, text="Enter city:")
city_entry = tk.Entry(window)
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
result_label = tk.Label(window, text="")

city_label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

window.mainloop()
