from django.db import models

# Create your models here.

class Offer(models.Model):
      name = models.CharField(max_length=100)
      img = models.ImageField(upload_to='pics')
      desc = models.TextField()
      tempelate = models.CharField(max_length=100)

      def __str__(self):
          return 'Name:{0}   Description:{0} '.format(self.name,  self.desc)

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Engineer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contactme(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    date_reg1 = models.DateTimeField(verbose_name='date_reg1', auto_now_add=True)

    def __str__(self):
        return 'Name:{0} Email:{1} Subject:{0} Status:{0} '.format(self.name, self.email, self.subject, self.status)


class Feasable(models.Model):
    city = models.CharField(max_length=50, blank=False)
    building = models.CharField(max_length=50, blank=False)
    area = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=50, blank=False)


    def __str__(self):
        return 'City:{0} Building:{1} Area:{0} Pincode:{0} '.format(self.city, self.building, self.area, self.pincode)
