
## How to do experiment

- Setup local mysql by `mkdir mysql-db-data; docker-compose up`
- Launch Django Application by `bash gunicorn_start.sh`
- Launch Locus `locust -f load_test.py`
- Open browser to start load test: http://0.0.0.0:8089
- connect to local mysql to monitor general log

