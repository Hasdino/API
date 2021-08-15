docker-compose logs sql-server-db   - see problems

docker exec -it sql-server-db "bash" - log into container

docker-compose up -d      - build yml file


docker-compose down   -take down the yml file



docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container id     