FROM python:3.4-alpine

ADD ./shared /shared
ADD ./code /code
WORKDIR /code

#RUN apk add --update python3 py-pip\
#    && pip install -r requirements.txt \
#    && rm -rf /var/cache/apk/*

 RUN pip install -r requirements.txt

ADD crontab /etc/cron.d/fetch-data
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/fetch-data
# Create logfile
RUN touch /var/log/cron.log

CMD ["/usr/sbin/crond", "-f", "-d", "0"]
