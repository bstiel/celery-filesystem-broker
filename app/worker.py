import os
from celery import Celery


broker_url = os.getenv('CELERY_BROKER_URL', 'filesystem://')
broker_dir = os.getenv('CELERY_BROKER_FOLDER', './broker')

for f in ['out', 'processed']:
    if not os.path.exists(os.path.join(broker_dir, f)):
        os.makedirs(os.path.join(broker_dir, f))


app = Celery(__name__)
app.conf.update({
    'broker_url': broker_url,
    'broker_transport_options': {
        'data_folder_in': os.path.join(broker_dir, 'out'),
        'data_folder_out': os.path.join(broker_dir, 'out'),
        'data_folder_processed': os.path.join(broker_dir, 'processed')
    },
    'imports': ('tasks',),
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})
