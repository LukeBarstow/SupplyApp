from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django import forms
from django.utils import timezone
from .forms import StatusForm

from .models import Barracks, Floor, Bathroom, Item

def updateStatus(request):

    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = StatusForm()

        return render(request, "status.html", {'form': form})

def index(request):
    barracks_list = Barracks.objects.all()
    context = {'barracks_list': barracks_list,}
    return render(request, 'supply/index.html', context)

def floor(request, barracks_id):
    barracks = get_object_or_404(Barracks, pk=barracks_id)
    floor_list = Floor.objects.filter(barracks_id=barracks_id)
    context = {'floor_list': floor_list, 'barracks':barracks}
    return render(request, 'supply/floor.html', context)

def bathroom(request, barracks_id, floor_id):
    barracks = get_object_or_404(Barracks, pk=barracks_id)
    floor = get_object_or_404(Floor, pk=floor_id)
    bathroom_list = Bathroom.objects.filter(floor_id=floor_id)
    context = {'bathroom_list': bathroom_list,'floor':floor, 'barracks':barracks,}
    return render(request, 'supply/bathroom.html', context)

def statuses(request, barracks_id, floor_id, bathroom_id):
    barracks = get_object_or_404(Barracks, pk=barracks_id)
    floor = get_object_or_404(Floor, pk=floor_id)
    bathroom = get_object_or_404(Bathroom, pk=bathroom_id)
    item_list = Item.objects.filter(bathroom_id=bathroom_id)
    context = {'item_list':item_list,'bathroom': bathroom,'floor':floor, 'barracks':barracks,}
    return render(request, 'supply/status.html', context)

def update(request, barracks_id, floor_id, bathroom_id, item_id):
    barracks = get_object_or_404(Barracks, pk=barracks_id)
    floor = get_object_or_404(Floor, pk=floor_id)
    bathroom = get_object_or_404(Bathroom, pk=bathroom_id)
    item = get_object_or_404(Item, pk=item_id)
    status = Status.objects.filter(item_id=item_id)
    context = {'status':status,'item':item,'bathroom': bathroom,'floor':floor, 'barracks':barracks,}
    return render(request, 'supply/update.html', context)
