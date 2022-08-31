from django.urls import path
from nba import views


urlpatterns = [
  path("teams/", views.TeamList.as_view(), name="team_list"),
  path("teams/<int:pk>", views.TeamDetail.as_view(), name="team_detail"),
  path("players/", views.PlayerList.as_view(), name="player_list"),
  path("players/<int:pk>", views.PlayerList.as_view(), name="player_detail"),
  
]