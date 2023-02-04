from django.db import models

class Carrera911(models.Model):
    power = models.IntegerField
    acceleration = models.FloatField
    type_body = models.CharField(max_length=15)
