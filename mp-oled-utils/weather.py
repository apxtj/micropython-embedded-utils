import urequests

class Weather:
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=en"

    def get_weather(self):
        try:
            res = urequests.get(self.url)
            if res.status_code == 200:
                data = res.json()
                res.close()
                temp = data['main']['temp']
                weather_condition = data['weather'][0]['main']
                desc = data['weather'][0]['description']
                return temp, weather_condition, desc
        except Exception as e:
            print(f"Weather API Error: {e}")
        return None, None, None
