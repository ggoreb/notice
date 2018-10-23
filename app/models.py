from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    c_date = models.DateTimeField()