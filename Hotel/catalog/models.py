from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=3)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()


    def __str__(self):
        return self.room_number

class Guest(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    objects = models.Manager()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.guest} - Room {self.room.room_number}"