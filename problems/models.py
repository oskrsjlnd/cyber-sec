from django.db import models

# Create your models here.
class Account(models.Model):
    user = models.CharField(max_length=200, unique=True)
    # Passwords are not stored with secure hashing and functions
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user + self.password

class Diary(models.Model):
    user = models.CharField(max_length=200)
    entry = models.TextField()

    def __str__(self):
        return self.entry
