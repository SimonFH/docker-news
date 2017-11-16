FROM python:3.4-alpine

RUN mkdir /shared
RUN touch /shared/data.json
ADD ./code /code
#RUN chmod 644 /code/fetch-data.py
WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "fetch-data.py"]

#ADD crontab /etc/cron.d/fetch-data
# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/fetch-data
#RUN echo '*/5 * * * * root python /code/fetch-data.py >> /code/fetch-data.log 2>&1' > /etc/crontabs/root
# Create logfile
#RUN touch /var/log/cron.log
 
# Run the command on container startup
#CMD ["/usr/sbin/crond", "&&", "tail", "-f", "/var/log/cron.log"]
#CMD ["/usr/sbin/crond", "-f", "-d", "0"]
#RUN echo '*  *  *  *  *    /usr/local/bin/myawesomescript' > /etc/crontabs/root
#CMD ["/usr/sbin/crond", "-l 2", "-f"]
