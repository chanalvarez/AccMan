from django.db import models

# Create your models here.
class Account(models.Model):
    title = models.CharField(max_length = 200)
    username = models.EmailField()
    password = models.CharField(max_length= 200)

    def __str__(self):
        return self.title

    