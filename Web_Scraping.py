#Web Scraping - collecting data from the websites
#Weather Scraping
import requests
headers = {'user-agent': 'Mozilla/70.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

ip_url = 'http://ip-api.com/json'

class deviceTracker():
    def __init__(self,ip_url):
        self.ip_url = ip_url
    def get_Device_Data(self):
        ip_req = requests.get(url = ip_url)
        if ip_req.status_code == 200:
            ip_data =  ip_req.json()
        else:
            ip_data = {}
        return ip_data
    def get_user_loc(self):
        ip_data  = self.get_Device_Data()
        city_name = ip_data['city']
        return city_name
ip_dev = deviceTracker(ip_url = ip_url)
city_name = ip_dev.get_user_loc()

class WeatherApp(deviceTracker):
    def __init__(self,ip_url):
        self.ip_url = ip_url
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ad3a2eeeb1a64b5315153af9b58e26d8'
        self.place_name  = None

    def get_Weather_data(self):
        self.place_name = input("Enter a valid City name : ")
        wea_url = self.weather_url.format(self.place_name)
        wea_req  = requests.get(url = wea_url)
        if wea_req.status_code == 200:
            wea_data = wea_req.json()
        else:
            print("-------------------------------------")
            print("The input is not valid.")
            print("Getting User Location...")
            self.place_name = self.get_user_loc()
            wea_url = self.weather_url.format(self.place_name)
            wea_req  = requests.get(url = wea_url)
            wea_data = wea_req.json()
        return wea_data

    def get_parsed_details(self):
        weather_data  = self.get_Weather_data()
        desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']

        celsius = temp-273
        farenheit = (celsius*(9/5))+32
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        all_clouds = weather_data['clouds']['all']

        print("The weather details of the place {} are :".format(self.place_name))
        print("The weather descriptions are :", desc)
        print("The weather temperature is {} celsius and {} farenheit".format((round(celsius,2)),(round(farenheit,2))))
        print("The wind speed is ",wind_speed)
        print("Humidity is ",humidity)
        print("Total Clouds : ",all_clouds)
        return True
w_app = WeatherApp(ip_url = ip_url)
w_app.get_parsed_details()

    
