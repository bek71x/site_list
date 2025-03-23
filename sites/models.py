from django.contrib.auth.models import User
from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=250)
    site = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title