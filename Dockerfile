#docker image to be extended to a new one
FROM python:3.9.5-alpine3.13
#optional information about who's maintaining this container
MAINTAINER MatteoFrigerio

#set to 1 the environment variable pythonbuffered, allowing the output to be printed 
#without being buffered
ENV PYTHONUNBUFFERED 1

#copy the requirements list from the workspace to the image
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
#install the requirements on the Docker image
RUN pip3 install -r /requirements.txt

#create a directory 'app' on the image
RUN mkdir /app
#set the 'app' directory on the image as the working directory (the app will run from here)
WORKDIR /app
#copy the source code (and all the other content in ./app in the workspace) to /app 
#on the image
COPY ./app /app

#create a user (-D option means that it will be used at runtime by docker, 
#and not by logged users) called username
RUN adduser -D mainUser
#switch docker to the created user (avoid running the root user is a good practice)
USER mainUser

