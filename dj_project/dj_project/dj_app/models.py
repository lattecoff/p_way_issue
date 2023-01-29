from django.db import models

class Carrera(models.Model):
    power = models.IntegerField()
    speed = models.IntegerField()
    acceleration = models.FloatField
    type_body = models.CharField(max_length=15)
