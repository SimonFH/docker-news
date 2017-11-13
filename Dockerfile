FROM python:3.4-alpine
ADD ./code /code
WORKDIR /code
RUN pip install -r requirements.txt
# Add crontab file to cron directory
ADD crontab /etc/cron.d/fetch-data
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/fetch-data
# Run on startup
CMD ["cron"]
CMD ["python", "app.py"]
