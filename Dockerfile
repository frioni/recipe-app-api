#docker image to extend to a new one
FROM python:3.7-alpine
#optional information about who's maintaining this container
MAINTAINER udemi frioni

#set to 1 the environment variable pythonbuffered, allowing the output to be printed 
#without being buffered
ENV PYTHONUNBUFFERED 1

#copy the requirements list from the workspace to the image
COPY ./requirements.txt /requirements.txt
#install the requirements on the Docker image
RUN pip3 install -r /requirements.txt

#create a directory 'app' on the image
RUN mkdir /app
#set the 'app' directory as the working directory (it will contain the source code)
WORKDIR /app
#copy the source code (and all the other content in ./app in the workspace) to /app 
#on the image
COPY ./app /app

#create a user (-D option means that it will be used at runtime by docker, 
#and not by logged users) called username
RUN adduser -D username
#switch docker to the created user (avoid running the root user is a good practice)
USER username

