from geotext import GeoText
sentence = "hyderabad is city in telangana"
sentence = sentence.upper()
print(sentence)
places = GeoText(sentence)
print(places.countries)
print(places.cities)