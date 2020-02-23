FROM python:3.6-slim

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python python-dev python-pip python-virtualenv && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./producer/ /home/root
WORKDIR /home/root

RUN pip install -r requirements.txt
