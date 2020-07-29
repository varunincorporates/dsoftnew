from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Uom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    mrp = models.IntegerField(default=1)
    prp = models.IntegerField(default=1)
    war = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    choices = {
        ('A', 'high value items'),
        ('B', 'Medium value items'),
        ('C', 'Low Value items')
    }

    abc = models.CharField(max_length=10, choices=choices, default='B')  # A, B, C

    choices = {
        ('F', 'fast moving items'),
        ('M', 'medium moving items'),
        ('S', 'slow moving items')
    }

    fms = models.CharField(max_length=1, choices=choices, default='M')  # F, M, Sww
    freezepur = models.BooleanField(default=False)
    freezesales = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    hnscode = models.CharField(max_length=10, default=1)
    gstper = models.IntegerField(default=18)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE)

    def __str__(self):
        return 'Product:{0} Mrp:{1} Description:{0} '.format(self.name, self.mrp, self.desc)
