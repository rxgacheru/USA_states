from django.shortcuts import render
from .models import State

# Create your views here.

def state_list(request):
    states = State.objects.all() if State.objects.exists() else []
    return render(request, 'states/state_list.html', {'states': states})




