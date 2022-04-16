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

    docker run -it -p <port_number_local>:<port_number_docker> --name <container_name> --mount source=<volume_name>,target=./app
