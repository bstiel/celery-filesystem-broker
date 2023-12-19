# The Filesystem as Celery Message broker

https://celery.school/filesystem-celery-message-broker

## Create and activate virtual environment

```bash
$ python -m venv venv
$ venv/bin/activate
$ pip install -r requirements.txt
```

## Start producer and worker

Using the Procfile:

```bash
$ honcho start
```

Without the Procfile, start the worker:

```bash
$ celery --app=worker.app worker --loglevel=INFO
```

Start the producer:

```bash
$ python producer.py
```
