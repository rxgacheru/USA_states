from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=2)
    region = models.IntegerField()
    division = models.CharField(max_length=100)

 