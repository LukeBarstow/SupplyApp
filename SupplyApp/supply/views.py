from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404

from .models import Barracks, Floor, Bathroom, Item, Status


def index(request):
    barracks_list = Barracks.objects.all()
    context = {'barracks_list': barracks_list,}
    return render(request, 'supply/index.html', context)

def floor(request, barracks_id):
    barracks = get_object_or_404(Barracks, pk=barracks_id)
    floor_list = Floor.objects.get(barracks_id=barracks_id)
    context = {'floor_list': floor_list,}
    return render(request, 'supply/floor.html', context)

def bathroom(request, floor_id):
    response = "Select your bathroom on %s."
    return HttpResponse(response % floor_id)

def statuses(request, bathroom_id):
    return HttpResponse("These are your supply levels for %s." % bathroom_id)

def update(request, bathroom_id):
    return HttpResponse("Update any of your bathroom's supply levels")
