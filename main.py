import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

track_number = phonenumbers.parse(number)
location = geocoder.description_for_number(track_number, "en")
service = phonenumbers.parse(number)
key = 'a2f72c70e358408a95cbbc647931edc2'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

 print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")



