from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),  
    path('fifth/', views.fifth, name='fifth'),    
    path('sixth/', views.sixth, name='sixth'),       
]