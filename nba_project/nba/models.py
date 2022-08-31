from django.db import models

# Create your models here.

class Conference(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
      return self.name

class Division(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
      return self.name
class Team(models.Model):
  name = models.CharField(max_length=100)
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="teams")
  division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="teams")
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
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
  

  

