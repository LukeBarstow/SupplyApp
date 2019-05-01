from django.contrib import admin

from .models import Barracks, Floor, Bathroom, Item

admin.site.register(Barracks)

admin.site.register(Floor)

admin.site.register(Bathroom)

admin.site.register(Item)
