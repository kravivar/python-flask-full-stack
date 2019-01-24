FROM python:3-alpine
RUN apk update
RUN apk add mysql-client git wget bash gcc musl-dev linux-headers nodejs git yarn
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN yarn global add bower
CMD ["bash", "/code/scripts/start.sh"]
