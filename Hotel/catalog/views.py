from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import*

from .forms import GuestForm
from .models import Guest

from .forms import BookingForm
from .models import Booking

from .forms import RoomForm
from .models import Room

from django.shortcuts import redirect


def info(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    return render(request, "info.html",{"guests": guests, "rooms": rooms, 'bookings': bookings})

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

def booking_new(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'booking_form': form})

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('info')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'booking_form': form, 'bookings': booking})


def booking_delete(request, pk):
    try:
        booking = Room.objects.get(pk=pk)
        booking.delete()
        return redirect('info')
    except Booking.DoesNotExist:
        return HttpResponseNotFound("<h2>Бронь не найдена</h2>")


