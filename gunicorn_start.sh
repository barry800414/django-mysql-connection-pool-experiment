#!/bin/bash

NAME="aiqua-ui-backend"                         # Name of the application
NUM_WORKERS=1                                   # how many worker processes should Gunicorn spawn
BIND_ADDR=${BIND_ADDR:-0.0.0.0:9200}

echo "Starting $NAME"

source ./venv/bin/activate

echo "starting myapp with django 2.2"
exec gunicorn -c gunicorn_config.py -w $NUM_WORKERS --bind=$BIND_ADDR mysite.wsgi
echo "started myapp"