# Docker Commands

    Note: In place of every <id> we can use <name> for containers and images

## Docker build

    docker build -t <image_name> <directory_path>

## Docker run

    docker run -it <image_name> <command>
    
    docker run -it -p <port_number_local>:<port_number_docker> <image_name> <command>

## List all running processes (containers)

    docker ps

    use docker ps -a to list all containers (running and stopped)

## Load container bash

    docker exec -it <container_id> /bin/sh

## Stop container

    docker stop <container_id>

## Delete container

    docker rm <container_id>

## Delete all stopped containers

    docker rm $(docker ps --filter status=exited -q)

## List all images

    docker images

## Delete image

    docker rmi <image_id>

## Create Docker Volume (Persistent Storage outside of Docker container)

    docker volume create <volume_name>

## List volumes

    docker volume ls

## Inspect volume

    docker volume inspect <volume_name>

## Remove a volume

    docker volume rm <volume_name>

## Run container with volume

    docer run -it -p <port_number_local>:<port_number_docker> -v <full_path_of_local_directory>:<WORKDIR_path> <image_name>

    docker run -it -p 8000:8000 -v "$(pwd)/app/":/app/ fastapi
