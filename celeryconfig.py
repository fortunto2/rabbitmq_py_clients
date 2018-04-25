## Broker settings.
# BROKER_URL = 'amqp://admin:LetMe!n@localhost:5672//'
BROKER_URL = 'amqp://admin:LetMe@q.life2film.com/'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('cel', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'

CELERY_ANNOTATIONS = {'*': {'rate_limit': '10/s'}}
