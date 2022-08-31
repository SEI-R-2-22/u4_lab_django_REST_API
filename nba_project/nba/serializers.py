from rest_framework import serializers
from nba.models import Team, Player

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  players = serializers.HyperlinkedRelatedField(view_name="player_detail", many=True, read_only=True)
  
  class Meta:
    model = Team
    fields=("id","name","city","state" ,"division","win" ,"loss", "players" )
    
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField( view_name="team_detail", read_only=True)
  
  class Meta:
    model = Player
    fields=("id", "team", "name","position","age" ,"injured" )