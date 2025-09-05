import requests

API_KEY = 'b7580e1ae0243e4d1290e9f0b967015b'  # <-- Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description']
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")
        else:
            print(f"City not found: {city}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)