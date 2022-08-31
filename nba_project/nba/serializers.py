from rest_framework import serializers
from nba.models import Team, Player, Conference, Division

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
  teams = serializers.HyperlinkedRelatedField(view_name="team_detail", many=True, read_only=True)
  
  class Meta:
    model = Conference
    fields=("id","name","teams")
class DivisionSerializer(serializers.HyperlinkedModelSerializer):
  teams = serializers.HyperlinkedRelatedField(view_name="team_detail", many=True, read_only=True)
  
  class Meta:
    model = Division
    fields=("id","name","teams")
class TeamSerializer(serializers.HyperlinkedModelSerializer):
  players = serializers.HyperlinkedRelatedField(view_name="player_detail", many=True, read_only=True)
  conference = serializers.HyperlinkedRelatedField(view_name="conference_detail", read_only=True)
  division = serializers.HyperlinkedRelatedField(view_name="division_detail", read_only=True)
  
  class Meta:
    model = Team
    fields=("id","name","city","state" ,"division","win" ,"loss", "players" )
    
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  team = serializers.HyperlinkedRelatedField( view_name="team_detail", read_only=True)
  
  class Meta:
    model = Player
    fields=("id", "team", "name","position","age" ,"injured" )