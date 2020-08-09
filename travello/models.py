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
    date_reg1 = models.DateTimeField(verbose_name='date_reg1', auto_now_add=True)

    def __str__(self):
        return 'Name:{0} Email:{1} Subject:{0}  '.format(self.name, self.email, self.subject)


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
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


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

