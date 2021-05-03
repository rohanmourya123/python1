import geocoder
import folium


IP = (input("enter the ip address "))
g = geocoder.ip(IP)
myAddress = g.latlng

myMap = folium.Map(location=myAddress,zoom_start=10)

folium.CircleMarker(location=myAddress,radius=30,popup="Yorkshire").add_to(myMap)

folium.Marker(location=myAddress,popup="Yorkshire").add_to(myMap)

# save  map to html file

myMap.save("mylocation.html")
