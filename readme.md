
docker run -it -e PBF_URL=http://download.geofabrik.de/north-america/us-northeast-latest.osm.pbf -e shm-size=8GB -p 8080:8080 --name nominatim mediagis/nominatim:4.2