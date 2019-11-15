from django.urls import path

from games import views

urlpatterns = [
    path(r'games/', views.game_list),
    path('games/<int:pk>/', views.game_detail),
]
#     path('snippets/<int:pk>/',
