FROM python:3.4-alpine

RUN mkdir /shared
RUN touch /shared/data.json
ADD ./code /code
#RUN chmod 644 /code/fetch-data.py
WORKDIR /code

RUN pip install -r requirements.txt

# Run data fetching script. 
# argv[1] is minutes to sleep between runs
CMD ["python", "fetch-data.py", "5"]

