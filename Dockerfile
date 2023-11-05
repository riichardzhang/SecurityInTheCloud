FROM ubuntu:22.04

WORKDIR /app/

RUN apt-get update
RUN apt-get install -y openjdk-17-jdk
RUN apt-get -y install python3-pip \
    && pip install boto3

COPY Main.java postgresql-42.6.0.jar getPassword.py /app/

CMD java -cp postgresql-42.6.0.jar Main.java $(python3 getPassword.py)
