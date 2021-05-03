

import phonenumbers
import folium
# from my_number import number
from phonenumbers import geocoder


region = input("enter the Region code ")
num= input("enter a phone number ");
print(region + num)
number = region + num



num = phonenumbers.parse(number)
location_of_number = geocoder.description_for_number(num,'en')
print(location_of_number)

# get service provider or mane of the sim use by  the user :
from phonenumbers import carrier

service = phonenumbers.parse(number)
print(carrier.name_for_number(service,"en"))


from opencage.geocoder import OpenCageGeocode

# we required a key:-

key = "ecbe2bd8865f4b389e409b887a07a874"

geocoder=OpenCageGeocode(key)

query1 = str(location_of_number)
result = geocoder.geocode(query1)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_stat = 10)
folium.Marker([lat,lng],popup=location_of_number).add_to((myMap))

# save  map to html file

myMap.save("mylocation.html")



