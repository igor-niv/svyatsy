from django.db import models

class Svyatsy(models.Model):
    sex = models.TextField()
    name = models.TextField()
    description = models.TextField()
    month = models.TextField()
    day = models.IntegerField()
