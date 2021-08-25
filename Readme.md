## Instructions

### DOCKER PART
ok this took a while. I wanted to use a mysql database but i ran into alot of problems, things to know:

docker-compose file:

`docker-compose up -d`

`docker ps`

`docker exec -it {container name} /bin/bash`

`mysql -u {user} -p`

and then you are inside a mysql shell:

Other important commands in case you run into problems:

`docker-compose logs {containerid} ` -to see problems

`docker-compose down -v`- NEVER do this or you lose your data.

`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container id ` - to check the ip of the container( not needed for this file since we did a port in the configuration)


***

the main issue was that i was losing my data after doing docker down even after trying to setup the docker with volumes and doing a named volume system, however it was not working. i found the issue after 2 days:

[for the issue of VOLUMES] (https://github.com/docker-library/mysql/issues/365#issuecomment-364908992)










