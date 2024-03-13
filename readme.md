# deps

```
poetry install
```

run:

```
docker run -it -e PBF_URL=http://download.geofabrik.de/north-america/us-northeast-latest.osm.pbf -e shm-size=8GB -p 8081:8080 --name nominatim mediagis/nominatim:4.3
```

(takes a while to initialize)

then

```
python main.py name-to-gpx.gpx
```
