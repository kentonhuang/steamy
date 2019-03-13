from django.urls import path
from . import views

urlpatterns = [
    path('api/game/', views.GameListCreate.as_view() ),
    path('api/game/<int:pk>', views.DetailGame.as_view()),
    path('api/steamuser/', views.SteamProfileList.as_view()),
    path('api/steamuser/<int:pk>', views.SteamProfileDetail.as_view()),
    path('api/testmodel/', views.TestList.as_view()),
    path('api/friends/<int:pk>', views.GetFriends.as_view()),
    path('api/shortprofile/', views.ShortProfiles.as_view()),
    path('api/badges', views.BadgesView.as_view()),
    path('api/badges/<int:pk>', views.GetBadges.as_view()),
]