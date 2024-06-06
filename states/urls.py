from django.urls import path
from . import views

urlpatterns = [
    path('', views.state_list, name='state_list'),
]
