import requests
import folium

ip = input("Enter IP address: ")

url = f"https://ipinfo.io/{ip}/json"
response = requests.get(url)
data = response.json()

city = data.get("city")
region = data.get("region")
country = data.get("country")
loc = data.get("loc")  # "lat,lng"

if not loc:
    print("Invalid IP address or location not found")
    exit()

lat, lng = map(float, loc.split(","))

print("City:", city)
print("Region:", region)
print("Country:", country)
print("Latitude:", lat)
print("Longitude:", lng)

myMap = folium.Map(location=[lat, lng], zoom_start=10)

popup_text = f"""
IP Address: {ip}<br>
City: {city}<br>
Region: {region}<br>
Country: {country}
"""

folium.Marker([lat, lng], popup=popup_text).add_to(myMap)

myMap.save("Geolocation_Tracker.html")
