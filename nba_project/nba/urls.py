from django.urls import path
from nba import views


urlpatterns = [
  path("teams/", views.TeamList.as_view(), name="team_list"),
  path("teams/<int:pk>", views.TeamDetail.as_view(), name="team_detail"),
  path("players/", views.PlayerList.as_view(), name="player_list"),
  path("players/<int:pk>", views.PlayerList.as_view(), name="player_detail"),
  path("conferences/", views.ConferenceList.as_view(), name="conference_list"),
  path("conference/<int:pk>", views.ConferenceList.as_view(), name="conference_detail"),
  path("division/", views.DivisionList.as_view(), name="division_list"),
  path("division/<int:pk>", views.DivisionList.as_view(), name="division_detail"),
  
]