from django.db import models

# Create your models here.


class Conference(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name='teams')
    wins = models.IntegerField(max_length=2)
    losses = models.IntegerField(max_length=2)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    injured = models.BooleanField()
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name
