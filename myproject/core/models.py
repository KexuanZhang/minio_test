from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', storage=S3Boto3Storage())
