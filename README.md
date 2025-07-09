# Stormforge

To run the project:

Obtain .env file 

Make sure you have docker installed and docker desktop running
Make sure you are logged into docker
Run:

    docker-compose up --build      

in root directory

Add -d flag to run in detached mode to not block terminal (Remember to stop the running container later with docker-compose down !!)

The docker-compose.yml configuration / script file will create two docker images (like a blueprint or file), one for frontend and one for backend.
It will then create a docker container (like a running instance) from the 2 images.
The docker container is self-contained (runs linux using your host) and thus should work the same in all different devices.


To stop the project:

    Ctrl+C      # to stop the running containers
    docker-compose down

To rerun the project after modifying code (without touching Dockerfile or dependencies):

    docker-compose up

To cleanly remove all docker containers:

    docker-compose down --volumes --remove-orphans
