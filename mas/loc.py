import geocoder
g = geocoder.ip('me')
print(g.latlng)


#example output
#--------------
#[9.9399, 76.2602]

#76.2602 -> Longitude
#9.9399  -> Latitude