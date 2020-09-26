from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('About/', views.About),
    path('Music/', views.Music),
    path('Coding/', views.Coding),
    path('Coding/CodingBotChat/', views.CodingBotChat),
    path('Coding/CodingWebDjango/', views.CodingWebDjango),
    path('Coding/CodingWebDjango_1/', views.CodingWebDjango_1),
    path('Coding/CodingWebDjango_2/', views.CodingWebDjango_2),
    path('Coding/CodingWebDjango_3/', views.CodingWebDjango_3),
    path('RedDragon16/', views.RedDragon16),
    path('RedDragon16/T3FPSMBGS/', views.T3FPSMBGS),
]