from django.db import models


class Barracks(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Floor(models.Model):
    barracks_id = models.ForeignKey(Barracks, on_delete=models.CASCADE, default='')
    floor = models.IntegerField()
    def __str__(self):
        return '%s %s' % (self.barracks_id, str(self.floor))

class Bathroom(models.Model):
    floor_id = models.ForeignKey(Floor, on_delete=models.CASCADE, default='')
    bathroom = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.floor_id, self.bathroom)

class Item(models.Model):
    bathroom_id = models.ForeignKey(Bathroom, on_delete=models.CASCADE, default='')
    item = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' % (self.bathroom_id, self.item)

class Status(models.Model):
    item_id = models.OneToOneField(Item, on_delete=models.CASCADE, default='')
    status = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s' % (self.item_id, self.status)
