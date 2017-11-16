FROM python:3.4-alpine
ADD ./shared /shared
ADD ./code /code
WORKDIR /code
# Install python packages
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
