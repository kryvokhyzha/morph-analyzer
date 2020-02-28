FROM alpine:3.7

# Install Python and OpenJDK 8
RUN apk add --update \
    python3 \
    python3-dev \
    py-pip \
    build-base \
    openjdk8-jre \
    && rm -rf /var/cache/apk/*

COPY . /home/root
WORKDIR /home/root

ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apk add --no-cache bash bash-doc bash-completion

RUN pip3 install --upgrade pip==20.0.2
RUN pip3 install -r requirements.txt
