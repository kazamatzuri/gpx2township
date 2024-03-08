from geopy.geocoders import Nominatim
import gpxpy

VILLAGES=set()
TOWNSHIPS=set()
CITIES=set()
STATES=set()
geolocator = Nominatim(domain='localhost:8080/', scheme='http',user_agent="myGeocoder")

def get_township(lat, lon):

    # geolocator = Nominatim(domain='localhost:8080/nominatim', scheme='http',user_agent="myGeocoder")    
    location = geolocator.reverse([lat, lon], exactly_one=True)
    
    if location is None:
        return None
    address = location.raw['address']
    
    city = address.get('city', '')
    village = address.get('village', '')
    township = address.get('township', '')
    loc={"city":city,"village":village,"township":township,"state":address.get('state', '')}
    return loc    

def parse_gpx_file(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                loc=get_township(point.latitude, point.longitude)
                if loc is None:
                    continue
                VILLAGES.add(loc["village"])
                TOWNSHIPS.add(loc["township"])
                CITIES.add(loc["city"])
                STATES.add(loc["state"])
                # print('Lat/Lon:', point.latitude, point.longitude)

# Example usage:
file="TAT FAB 2023.gpx"
parse_gpx_file(file)

print("STATES")
for s in STATES:
    print(s)
# print("VILLAGES")
# for v in VILLAGES:
#     print(v)
# print("TOWNSHIPS")
# for t in TOWNSHIPS:
#     print(t)
# print("CITIES")
# for c in CITIES:
#     print(c)
# print(get_township(43.4805667, -071.7565000))  # Coordinates for New York City
