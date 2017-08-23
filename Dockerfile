FROM python:2.7-alpine
RUN apk update
RUN apk add mysql-client git wget bash gcc musl-dev linux-headers nodejs git
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN npm install bower -g
CMD ["bash", "/code/scripts/start.sh"]
