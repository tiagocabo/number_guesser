FROM  python:3.9-slim

WORKDIR /usr/local/python/number_guesser/

COPY envs/linux/Pipfile ./
COPY ML_api.py CNN_v0.model ./

EXPOSE 8080
RUN apt-get update
ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

CMD python ML_api.py
ENTRYPOINT [ "venv/bin/python" , "ML_api.py"]