from django.db import models
from django.db.models.signals import post_save
import threading
import time


class Post(models.Model):
    title = models.CharField(max_length=120, default="")


def save_post(sender, instance, **kwargs):
    print("post save message this is done. This prove Answer 1") # Signal handler code answer 1
    time.sleep(5) # for checking that task running in same instance
    print(f"Signal handler thread ID: {threading.get_ident()} This prove Answer 2")  # Thread ID inside the signal handler
    

post_save.connect(save_post, sender=Post)
