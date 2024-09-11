from django.db import models
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(pre_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler called")
    # Let's try to raise an exception to test the rollback
    raise Exception("Rolling back transaction")