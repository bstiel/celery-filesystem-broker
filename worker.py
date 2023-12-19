import os
from celery import Celery


path = "./.data/broker"
if not os.path.exists(path):
    os.makedirs(path)


app = Celery(
    __name__,
    broker_url="filesystem://",
    broker_transport_options={
        "data_folder_in": path,
        "data_folder_out": path,
    },
    imports=("tasks",),
)
