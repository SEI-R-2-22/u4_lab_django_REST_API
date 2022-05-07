from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.CharField(max_length=20)
    wins = models.IntegerField(max_length=3)
    losses = models.IntegerField(max_length=3)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    injured = models.BooleanField()

    def __str__(self):
        return self.name
