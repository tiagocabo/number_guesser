FROM  python:3.9

LABEL MAINTAINER="Tiago Cabo"

COPY . /usr/local/python/number_guesser/

EXPOSE 8080
WORKDIR /usr/local/python/number_guesser/
RUN apt-get update
ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN python3 -m pip install --upgrade pip


RUN python3 -m pip install pipenv
RUN pipenv install --system --skip-lock # to avoid venv definition
CMD python ML_api.py

ENTRYPOINT [ "python" , "ML_api.py"]