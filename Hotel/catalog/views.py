from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import*

from .forms import GuestForm
from .models import Guest

from .forms import RoomForm
from .models import Room

from django.shortcuts import redirect


def info(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    return render(request, "info.html",{"guests": guests, "rooms": rooms})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guest_details.html', {'guest': guest})

def guest_new(request):
    form = GuestForm()
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = GuestForm()
    return render(request, 'guest_form.html', {'guest_form': form})

def guest_edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.save()
            return redirect('guest_detail', pk=guest.pk)
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guest_form.html', {'guest_form': form, 'guest': guest})

def guest_delete(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return redirect('info')
    except Guest.DoesNotExist:
        return HttpResponseNotFound("<h2>Гость не найден</h2>")

def room_new(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'room_form': form})

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('info.html')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_form.html', {'room_form': form, 'room': room})


def room_delete(request, pk):
    try:
        room = Room.objects.get(pk=pk)
        room.delete()
        return redirect('info')
    except Room.DoesNotExist:
        return HttpResponseNotFound("<h2>Комната не найдена</h2>")


