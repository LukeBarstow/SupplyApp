from django.contrib import admin

from .models import Barracks, Floor, Bathroom, Item, Status

admin.site.register(Barracks)

admin.site.register(Floor)

admin.site.register(Bathroom)

admin.site.register(Item)

admin.site.register(Status)
