from django import forms
from .models import Room
from .models import Guest
from .models import Booking

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields=('firstname', 'lastname','email','phone_number')
        labels ={
            'firstname': "Имя",
            'lastname': "Фамилия",
            'email': "E-mail",
            'phone_number': "Номер телефона",
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'имя'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'фамилия'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '8'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        capacity_choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
        model = Guest
        fields=('room_number', 'capacity','price_per_night')
        labels ={
            'room_number': "Номер комнаты",
            'capacity': "Кол-во проживающих",
            'price_per_night': "Цена за сутки",
        }
        widgets = {
            'capacity': forms.RadioSelect(attrs={'name': 'gender'}, choices=capacity_choices),
            'room_number': forms.TextInput(attrs={'placeholder': 'руб'}),
        }