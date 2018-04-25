from celery import Celery

# app = Celery('tasks', broker='pyamqp://admin@localhost//')
# app = Celery('tasks', backend='amqp', broker='amqp://')
# app = Celery('hello', broker='amqp://admin:LetMe@localhost:5672/')
app = Celery('hello', broker='amqp://admin:LetMe@q.life2film.com/')

@app.task
def hello():
    print('start')
    return 'hello world'
