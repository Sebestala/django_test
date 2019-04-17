from django.shortcuts import render
from .models import ActivitiesForm, SportForm

def activities(request):
    """ Différentes activités """
    return render(request, "activities/activities.html")
