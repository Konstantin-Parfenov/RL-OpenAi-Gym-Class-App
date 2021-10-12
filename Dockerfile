# start from base
FROM python:3.7.2-alpine3.8
LABEL maintainer="parkonst@gmail.com"
ENV ADMIN="Konstantin Parfenov"
# Update base layer
RUN apk update && apk upgrade && apk add bash

# Install native libraries, required for numpy and curl to test API
RUN apk --no-cache add musl-dev linux-headers g++ curl
# Upgrade pip
RUN pip install --upgrade pip
# Copy and install requirements
COPY /requirements.txt .
RUN pip install -r requirements.txt
# Copy application files
COPY . ./app
# Open port 5000 in container is run with -P argument
EXPOSE 5000
# Start application
CMD ["python", "./app/app.py"]
