
from rest_framework import generics
from nba.serializers import TeamSerializer, PlayerSerializer, ConferenceSerializer, DivisionSerializer
from nba.models import Division, Team, Player, Conference

# Create your views here.

class TeamList(generics.ListCreateAPIView):
  queryset=Team.objects.all()
  serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
  queryset= Player.objects.all()
  serializer_class = PlayerSerializer

class ConferenceList(generics.ListCreateAPIView):
  queryset= Conference.objects.all()
  serializer_class = ConferenceSerializer
  
class DivisionList(generics.ListCreateAPIView):
  queryset= Division.objects.all()
  serializer_class = DivisionSerializer
  
class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
  
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Player.objects.all()
  serializer_class = PlayerSerializer
  
class ConferenceList(generics.RetrieveUpdateDestroyAPIView):
  queryset = Conference.objects.all()
  serializer_class = ConferenceSerializer
class DivisionList(generics.RetrieveUpdateDestroyAPIView):
  queryset = Division.objects.all()
  serializer_class = DivisionSerializer
