# usamos as para poner un alias
from .celery import app as celery_app

__all__ = ('celery_app',)

# Se puede ejecutar de las 2 maneras

# celery -A school-celery worker -l info

# celery -A school worker -l info




