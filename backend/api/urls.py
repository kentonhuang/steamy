from django.urls import path
from . import views

urlpatterns = [
    path('api/game/', views.GameListCreate.as_view() ),
    path('api/game/<int:pk>', views.DetailTodo.as_view()),
]