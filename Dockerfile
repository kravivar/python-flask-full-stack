FROM python:2.7-alpine
RUN apk update
RUN apk add mysql-client git wget bash
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["bash", "/code/scripts/wait-for-it.sh", "-s", "-t", "120", "-h", "mysql", "-p", "3306", "--", "python", "run.py"]
