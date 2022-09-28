from django.db import models

# Create your models here.


class Articles(models.Model):
    content = models.TextField()
