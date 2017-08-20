#!/bin/bash

if [[ "$FLASK_ENVIRONMENT" == "stage" ]]
then
  bash /code/scripts/wait-for-it.sh -s -t 120 -h mysql -p 3306 -- python /code/run.py
else
  python /code/run.py
fi