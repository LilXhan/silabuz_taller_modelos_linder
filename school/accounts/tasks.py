from celery import shared_task
import time 
# shared_task es un decorador que nos permite crear una tarea

@shared_task
def sum(x, y):
    time.sleep(10)
    return x + y