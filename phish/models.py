from django.db import models

# Create your models here.
class report(models.Model):
    phished_url = models.URLField()
    email = models.EmailField(max_length=30)
    comment = models.TextField(max_length=30)