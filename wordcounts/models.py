from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
