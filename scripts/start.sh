#!/bin/bash

if [[ "$FLASK_ENVIRONMENT" == "stage" ]]
then
	bash /code/scripts/wait-for-it.sh -s -t 120 -h mysql -p 3306 -- cd /code && uwsgi --socket 0.0.0.0:5000 --protocol=http -w run:app
	#bash /code/scripts/wait-for-it.sh -s -t 120 -h mysql -p 3306 -- python /code/run.py
else
	uwsgi --socket 0.0.0.0:5000 --protocol=http -w run:app
	#python /code/run.py
fi