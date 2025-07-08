from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()
