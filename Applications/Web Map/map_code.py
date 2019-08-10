import folium
import os
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location = [39, -99],zoom_start = 6, tiles = "Mapbox Bright")
fg = folium.FeatureGroup(name = "World Population")
fg1 = folium.FeatureGroup(name = "Volcanoes")


def colour(el):
    if el <1000 :
        return "green"
    elif 1000<= el <2000:
        return "blue"
    else:
        return "red"


for lt,ln,el in zip(lat,lon,elev):
    fg1.add_child(folium.Marker(location = [lt,ln], popup = str(el)+" Metres", icon =folium.Icon(color = colour(el) )  ))

fg.add_child(folium.GeoJson(data =open('world.json','r',encoding = 'utf-8-sig').read(),
                style_function = lambda x:{'fillColor' : 'green' if x["properties"]["POP2005"]<10000000
                else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"  }  ))

map.add_child(fg1)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
