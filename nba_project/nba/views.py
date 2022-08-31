
from rest_framework import generics
from nba.serializers import TeamSerializer, PlayerSerializer
from nba.models import Team, Player

# Create your views here.

class TeamList(generics.ListCreateAPIView):
  queryset=Team.objects.all()
  serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
  queryset= Player.objects.all()
  serializer_class = PlayerSerializer
  
class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
  
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer
