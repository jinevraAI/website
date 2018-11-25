from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email_address = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email_address
