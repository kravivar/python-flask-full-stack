FROM python:3-alpine
RUN apk update
RUN apk add mysql-client git wget bash gcc musl-dev linux-headers nodejs git yarn g++
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["bash", "/code/scripts/start.sh"]
