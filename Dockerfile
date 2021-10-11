# start from base

FROM python:3.7.2-alpine3.8
LABEL maintainer="omg@gmail.com"
ENV ADMIN="omg"
RUN apk update && apk upgrade && apk add bash

# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++ curl

RUN pip install --upgrade pip
COPY /requirements.txt .
RUN pip install -r requirements.txt
COPY . ./app
EXPOSE 5000
CMD ["python", "./app/app.py"]
