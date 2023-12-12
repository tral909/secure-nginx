FROM python:alpine3.19
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python3 app.py

# docker build -t web .