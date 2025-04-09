from celery import shared_task

@shared_task
def my_task():
    print("Celery task is working!")
    return "Task completed"
