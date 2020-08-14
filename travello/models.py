from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()


class Offer(models.Model):
      name = models.CharField(max_length=100)
      img = models.ImageField(upload_to='pics')
      desc = models.TextField()
      tempelate = models.CharField(max_length=100)

      def __str__(self):
          return 'Name:{0}   Description:{0} '.format(self.name,  self.desc)

class Complain(models.Model):
    name= models.CharField(max_length=100, blank=False)
    mobile= models.CharField(max_length=25, blank=False)
    email= models.CharField(max_length=25, blank=False)
    accountno = models.CharField(max_length=25, blank=False)
    category = models.CharField(max_length=200, null=True)
    subject =  models.CharField(max_length=200, null=True)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True)
    date_solved = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField()

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Newcustomer(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.TextField()
    mobileno = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    adharcardno =  models.CharField(max_length=20)
    adharcard = models.ImageField(upload_to='pics')
    panno = models.CharField(max_length=20)
    pan = models.ImageField(upload_to='pics')
    drivinglicenceno = models.CharField(max_length=20)
    drivinglicence = models.ImageField(upload_to='pics')
    electricityno = models.CharField(max_length=20)
    electricitybill = models.ImageField(upload_to='pics')
    active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return  self.name


class Engineer(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Contactme(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message =  models.TextField()
    date_reg1 = models.DateTimeField(auto_now_add=True)




class Referal(models.Model):
    myname = models.CharField(max_length=50, blank=False)
    mymobile = models.CharField(max_length=20)
    referalname = models.CharField(max_length=50, blank=False)
    referalmobile = models.CharField(max_length=20)
    referalemail = models.EmailField(max_length=60)
    referaladdress = models.TextField()
    message = models.TextField()
    category = models.CharField(max_length=25)
    contacttime = models.CharField(max_length=30)
    date_reg1 = models.DateTimeField(verbose_name='date_reg1', auto_now_add=True)

    def __str__(self):
        return self.referalname, self.referalmobile


class Feasable(models.Model):
    city = models.CharField(max_length=50, blank=False)
    building = models.CharField(max_length=50, blank=False)
    area = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=50, blank=False)


    def __str__(self):
        return 'City:{0} Building:{1} Area:{0} Pincode:{0} '.format(self.city, self.building, self.area, self.pincode)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    benefits = models.CharField(max_length=150, blank=False)
    validity = models.CharField(max_length=150, blank=False)
    value = models.IntegerField()

    def __str__(self):
        return self.benefits


class Salesfaq(models.Model):
    Type = models.CharField(max_length=25, blank=False)
    serial = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.question


class Order(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


    def __str__(self):
        return self.status


class Myorder(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Progress', 'Progress'),
        ('Installed', 'Installed'),
    }
    name = models.ForeignKey(Newcustomer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.name, self.product, self.note


class Newcomplain(models.Model):
    name = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=60)
    accountno = models.CharField(max_length=100, blank=False)
    STATUS = {
        ('No Connection', 'No Connection'),
        ('Slow Speed', 'Slow Speed'),
        ('Billing Complant', 'Billing Complant'),
        ('Relocation', 'Relocation'),
    }
    category = models.CharField(max_length=200, null=True, choices=STATUS)
    STATUS1= {
        ('UNABLE TO BROWSE','UNABLE TO BROWSE'),
        ('PASSWORD FORGOT','PASSWORD FORGOT'),
        ('WEBSITE NOT OPENING','WEBSITE NOT OPENING'),
        ('CABLE CUT','CABLE CUT'),
        ('EQUIPEMENT PROBLEM','EQUIPEMENT PROBLEM'),
        ('FREQUENTLY DISCONNECT','FREQUENTLY DISCONNECT'),
        ('ROUTER SUPPORT','ROUTER SUPPORT'),
        ('BILL DISPUTE', 'BILL DISPUTE'),
        ('PAYMENT NOT UPDATED','PAYMENT NOT UPDATED'),
        ('PAYMENT PROBLEM','PAYMENT PROBLEM'),
        ('SLOW SPEED TEST','SLOW SPEED TEST'),
    }
    subject = models.CharField(max_length=200, null=True, choices=STATUS1)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True,default='PENDING')
    date_solved = models.DateTimeField(null=True)
    note = models.TextField()
    comments=models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.id, self.name, self.mobile, self.note