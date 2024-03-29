from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    type = models.CharField(max_length=10, default='day')
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.text