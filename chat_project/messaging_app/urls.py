from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:user2_id>', views.room_name, name='room_name'),

    
]
