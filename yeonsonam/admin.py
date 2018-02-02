from django.contrib import admin

from .models import Drama, Seat_photo, Price, Genre, Site_reservation, Discount,Place, Sequence, Actor
# Register your models here.

admin.site.register(Drama)
admin.site.register(Seat_photo)
admin.site.register(Price)
admin.site.register(Genre)
admin.site.register(Site_reservation)
admin.site.register(Discount)
admin.site.register(Place)
admin.site.register(Actor)
admin.site.register(Sequence)