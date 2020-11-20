FROM tensorflow/tensorflow

MAINTAINER Tiago Cabo

COPY . /usr/local/python/number_guesser/

EXPOSE 5000
WORKDIR /usr/local/python/number_guesser/
RUN apt-get update
ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y install python3-tk
RUN python3 -m pip install --upgrade pip


RUN python3 -m pip install -r requirements.txt
CMD python test_model.py