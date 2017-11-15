FROM python:3.4-alpine
#FROM ubuntu:latest
#FROM alpine:latest
#RUN apk add --update python py-pip && rm -rf /var/cache/apk/*
#RUN sudo apt-get install python
ADD ./shared /shared
ADD ./code /code
WORKDIR /code
# Install python packages
RUN pip install -r requirements.txt
## Install cron
##RUN apt-get update && apt-get -y install cron
### Add crontab file to cron directory
#ADD crontab /etc/cron.d/fetch-data
## Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/fetch-data
## Create logfile
#RUN touch /var/log/cron.log
# Run on startup
CMD ["python", "app.py"]
