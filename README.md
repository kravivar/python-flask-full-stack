# python-flask-full-stack
Full stack python example

## Pre-requesites
* git
* docker toolbox

## Getting started
* Clone the repository
``` git clone https://github.com/kravivar/python-flask-full-stack.git```
* Run docker-compose to bring the stack up
```
Running stack with sqllite DB

# cd python-flask-full-stack
# docker-compose up

Running stack with mysql database

# cd python-flask-full-stack
# docker-compose -f stage-docker-compose.yml up
```

## Example API calls
* GET - `curl http://localhost/api/dev/`
* GET with id - `curl http://localhost/api/dev/?id=1`
* POST - `curl -X POST -H 'Content-Type: application/json' -d '{"name":"kripa","focus":"scientist"}' http://localhost/api/dev/`
* DELETE - `curl -X DELETE http://localhost/api/dev/?id=15`

## References
### API
* http://www.bradcypert.com/writing-a-restful-api-in-flask-sqlalchemy/
### UI
* https://github.com/puikinsh/gentelella

