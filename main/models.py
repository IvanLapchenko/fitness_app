from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    about = models.CharField(max_length=512)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.username = name
        # self.email = email
        # self.about = about
        # self.password = password


class Exercise(models.Model):
    description = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    image = models.CharField(max_length=128)


class Workout(models.Model):
    description = models.CharField(max_length=512)
    name = models.CharField(max_length=128)


class WorkoutData(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
