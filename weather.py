import urllib.request
import json

# Partners: Jordin Stephens and Khylan
# Hometown: Los Angeles, CA

latitude = 34.0522
longitude = -118.2437

url = ("https://api.open-meteo.com/v1/forecast?latitude=" + str(latitude)
       + "&longitude=" + str(longitude)
       + "&hourly=temperature_2m,precipitation_probability"
       + "&temperature_unit=fahrenheit&timezone=America%2FNew_York&forecast_days=2")

response = urllib.request.urlopen(url, timeout=15)
data = json.loads(response.read())

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
rain = data["hourly"]["precipitation_probability"]

print(len(times), "hours of forecast")

for i in range(len(times)):
    print(times[i], temps[i], "F")

temperature = float(input("Enter a temperature: "))

count = 0
for temp in temps:
    if temp >= temperature:
        count += 1

print(count, "hours at or above", temperature, "F")

hottest_temp = temps[0]
hottest_time = times[0]

for i in range(1, len(temps)):
    if temps[i] > hottest_temp:
        hottest_temp = temps[i]
        hottest_time = times[i]

print("Hottest hour:", hottest_time, hottest_temp, "F")

for i in range(len(rain)):
    if rain[i] >= 50:
        print("First rain chance of 50% or more:", times[i], rain[i], "%")
        break
else:
    print("No rain likely today or tomorrow")