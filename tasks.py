import random
from worker import app


@app.task(bind=True, name='long_running_task')
def long_running_task(self):
    n = 100000
    total = 0
    for i in range(0, n):
        total += random.randint(1, 1000)
    return total / n
