import phonenumbers
import folium
from folium import Map

from myNumber import number

from phonenumbers import geocoder
Key = "ec2a3f14de9a425da376bcdd12e296a4"

tomNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(tomNumber,"en")
print(yourLocation)

# Service Provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

# Save map in html file
myMap.save("my_Location.html")