# ProFinansy test task

## Description

Need: write project using fastapi, with has 3 routes.

1 - got x, y and operator (return task id)

2 - got task id from 1 route (return task status)

3 - return all tasks with statuses

## Installing and running

1. clone the repo using `git clone https://github.com/romaokorosso/test_task_profinansy`
2. `cd test_task_profinansy`

For running in console:
1. run `pip install -r requirements.txt`
2. run tests `pytest tests.py`
3. run `uvicorn main:app`

For running in Docker:
1. run `docker-compose up -d`

Then:
1. visit 'http://0.0.0.0:8000/' or 'http://0.0.0.0:8000/docs'
