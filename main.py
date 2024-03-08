import argparse
from geopy.geocoders import Nominatim
import gpxpy

VILLAGES = set()
TOWNSHIPS = set()
CITIES = set()
STATES = set()
geolocator = Nominatim(domain="localhost:8080/", scheme="http", user_agent="myGeocoder")


def get_township(latitude, longitude):

    # geolocator = Nominatim(domain='localhost:8080/nominatim', scheme='http',user_agent="myGeocoder")
    location = geolocator.reverse([latitude, longitude], exactly_one=True)

    if location is None:
        return None
    address = location.raw["address"]

    city = address.get("city", "")
    village = address.get("village", "")
    township = address.get("township", "")
    location_info = {
        "city": city,
        "village": village,
        "township": township,
        "state": address.get("state", ""),
    }
    return location_info


def parse_gpx_file(gpx_file_path):
    with open(gpx_file_path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                location_info = get_township(point.latitude, point.longitude)
                if location_info is None:
                    continue
                VILLAGES.add(location_info["village"])
                TOWNSHIPS.add(location_info["township"])
                CITIES.add(location_info["city"])
                STATES.add(location_info["state"])
                # print('Lat/Lon:', point.latitude, point.longitude)


def main():
    parser = argparse.ArgumentParser(
        description="Parse a GPX file and extract township information."
    )
    parser.add_argument("gpx_file_path", help="The path to the GPX file to parse.")
    args = parser.parse_args()

    parse_gpx_file(args.gpx_file_path)

    print("STATES")
    for s in STATES:
        print(s)
    print("VILLAGES")
    for v in VILLAGES:
        print(v)
    print("TOWNSHIPS")
    for t in TOWNSHIPS:
        print(t)
    # print("CITIES")
    # for c in CITIES:
    #     print(c)
    # print(get_township(43.4805667, -071.7565000))  # Coordinates for New York City


if __name__ == "__main__":
    main()
