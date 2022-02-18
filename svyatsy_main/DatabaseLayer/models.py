from django.db import models

# Модель БД для ORM
class Svyatsy(models.Model):
    sex = models.TextField()
    name = models.TextField()
    description = models.TextField()
    month = models.TextField()
    day = models.IntegerField()
