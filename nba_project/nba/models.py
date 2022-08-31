from django.db import models

# Create your models here.

class Team(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  division = models.CharField(max_length=100)
  win = models.IntegerField()
  loss = models.IntegerField()
  
  def __str__(self):
      return self.name
  
class Player(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
  name = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  age = models.IntegerField()
  injured = models.BooleanField()
  
  def __str__(self):
      return self.name
  

