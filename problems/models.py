from django.db import models
# Create your models here.

class Account(models.Model):
    user = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user + self.password

class Diary(models.Model):
    user = models.CharField(max_length=200)
    entry = models.TextField()

    def __str__(self):
        return self.entry

# FIX FOR LOGGING
# class UserLogs(models.Model):
    # user = models.CharField(max_length=200)
    # time = models.TimeField()
    # event = models.CharField(max_length=64)
