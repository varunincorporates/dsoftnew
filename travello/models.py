from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User, auth


class Newsletter(models.Model):
    user1 = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = {
        ('Working', 'Working'),
        ('Resigned', 'Resigned'),
        ('OnContract', 'OnContract'),
        ('Temporary', 'Temporary'),
    }
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name, self.mobile, self.note


class Vendor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = {
        ('Working', 'Working'),
        ('Suspended', 'Suspended'),
        ('OnContract', 'OnContract'),
        ('Temporary', 'Temporary'),
    }
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name, self.mobile, self.note


class Employee1(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = {
        ('Working', 'Working'),
        ('Resigned', 'Resigned'),
        ('OnContract', 'OnContract'),
        ('Temporary', 'Temporary'),
    }
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name, self.mobile, self.note


class Newcomplain(models.Model):
    user1 = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
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
    STATUS1 = {
        ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'),
        ('PASSWORD FORGOT', 'PASSWORD FORGOT'),
        ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'),
        ('CABLE CUT', 'CABLE CUT'),
        ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'),
        ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'),
        ('ROUTER SUPPORT', 'ROUTER SUPPORT'),
        ('BILL DISPUTE', 'BILL DISPUTE'),
        ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'),
        ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'),
        ('SLOW SPEED TEST', 'SLOW SPEED TEST'),
    }
    subject = models.CharField(max_length=200, null=True, choices=STATUS1)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS2 = {
        ('OPEN', 'OPEN'),
        ('INPROGESS', 'INPROGRESS'),
        ('RESOLVED', 'RESOLVED'),
    }
    status = models.CharField(max_length=200, null=True, default='OPEN', choices=STATUS2)
    date_solved = models.DateTimeField(auto_now=True, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return self.id, self.name, self.mobile, self.note


class Newcomplain1(models.Model):
    user1 = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
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
    STATUS1 = {
        ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'),
        ('PASSWORD FORGOT', 'PASSWORD FORGOT'),
        ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'),
        ('CABLE CUT', 'CABLE CUT'),
        ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'),
        ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'),
        ('ROUTER SUPPORT', 'ROUTER SUPPORT'),
        ('BILL DISPUTE', 'BILL DISPUTE'),
        ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'),
        ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'),
        ('SLOW SPEED TEST', 'SLOW SPEED TEST'),
    }
    subject = models.CharField(max_length=200, null=True, choices=STATUS1)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS2 = {
        ('PENDING', 'PENDING'),
        ('SOLVED', 'SOLVED'),
        ('OBSERVATION', 'OBSERVATION'),
        ('VISIT', 'VISIT'),
        ('N.A.', 'N.A.'),
    }
    status = models.CharField(max_length=200, null=True, default='PENDING', choices=STATUS2)
    date_solved = models.DateTimeField(auto_now=True, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return self.id, self.name, self.mobile, self.note


class Newcustomer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, default="Pune")
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    STATUS2 = {
        ('MR', 'MR'),
        ('MS', 'MS'),
        ('MISS', 'MISS'),
        ('DR', 'DR'),
    }
    fathername = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True,choices=STATUS2)
    STATUS3 = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    }
    dob = models.DateTimeField(null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, default="India")
    gender = models.CharField(max_length=20, null=True, choices=STATUS3)
    STATUS4 = {
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
    }
    customertype = models.CharField(max_length=20, null=True, choices=STATUS4, default="Individual")
    STATUS5 = {
        ('Business', 'Business'),
        ('Residental', 'Residental'),
    }
    usage = models.CharField(max_length=20, null=True, choices=STATUS5, default="Residental")
    STATUS6 = {
        ('POSTPAID', 'POSTPAID'),
        ('PREPAID', 'PREPAID'),
    }
    connectiontype = models.CharField(max_length=20, null=True, choices=STATUS6, default="POSTPAID")
    STATUS7 = {
        ('Email', 'Email'),
        ('Mobile', 'Mobile'),
    }
    communicationmethod = models.CharField(max_length=20, null=True, choices=STATUS7, default="Email")
    accsubtype =  models.CharField(max_length=100, null=True)
    STATUS20 = {
        ('Monthly', 'Monthly'),
        ('Bimonthly', 'Bimonthly'),
    }
    frequency = models.CharField(max_length=30,null=True, choices=STATUS20, default="Monthly")
    STATUS21 = {
        ('EMAIL', 'EMAIL'),
        ('Print Bill On Paper', 'Print Bill On Paper'),
        ('PAPER AND EMAIL','PAPER AND EMAIL'),
    }
    billmedia = models.CharField(max_length=20, null=True, choices=STATUS21, default="EMAIL")
    STATUS22 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card','Voter ID Card' ),
        ('Goverment ID Card','Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer','Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card','PAN Card'),
        ('Photo ID by Village Panchayath','Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO','Pass Book Of Bank or PO'),
        ('Passport','Passport'),
        ('Ration Card with Photo','Ration Card with Photo'),
        ('Photo ID Card by Edu Institute','Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence','Smart Card by CSD Defence'),
    }
    poi = models.CharField(max_length=50, null=True, choices=STATUS22)
    poitype = models.CharField(max_length=100, null=True)
    poiref = models.CharField(max_length=100, null=True)
    STATUS23 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer','Issued By MLA MP GR A Officer'),
        ('Income Tax Department','Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poiby = models.CharField(max_length=100, null=True,choices=STATUS23)
    poidate = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    STATUS32 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card', 'Voter ID Card'),
        ('Goverment ID Card', 'Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card', 'PAN Card'),
        ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'),
        ('Passport', 'Passport'),
        ('Ration Card with Photo', 'Ration Card with Photo'),
        ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'),
    }
    poa = models.CharField(max_length=50, null=True, choices=STATUS32)
    poatype = models.CharField(max_length=100, null=True)
    poaref = models.CharField(max_length=100, null=True)
    STATUS33 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'),
        ('Income Tax Department', 'Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poaby = models.CharField(max_length=100, null=True, choices=STATUS33)
    poadate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    billemail = models.CharField(max_length=20, null=True)
    uesrname = models.CharField(max_length=200, null=True, blank=True)
    mobileno = models.CharField(max_length=20, null=True, default="123")
    mobileno1 = models.CharField(max_length=20, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True)
    houseno = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, default="Pune")
    district = models.CharField(max_length=100, default="Pune")
    locaility = models.CharField(max_length=100, default="Pune")
    sublocaility = models.CharField(max_length=100, default="Pune")
    exchangecode  = models.CharField(max_length=100, default="Pune")
    STATUS8 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    ccategory = models.CharField(max_length=100, choices=STATUS8,  default="Urban")
    state = models.CharField(max_length=100, default="Maharashtra")
    gstin = models.CharField(max_length=15, default="27")

    bpincode = models.CharField(max_length=20, null=True, blank=True)
    bhouseno = models.CharField(max_length=100, null=True, blank=True)
    bvillage = models.CharField(max_length=100, null=True, blank=True)
    blandmark = models.CharField(max_length=100, null=True, blank=True)
    bcity = models.CharField(max_length=100, default="Pune", blank=True)
    baddress = models.CharField(max_length=500, default="Pune", blank=True)
    bdistrict = models.CharField(max_length=100, default="Pune", blank=True)
    blocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bsublocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bexchangecode = models.CharField(max_length=100, default="Pune", blank=True)
    STATUS48 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    bccategory = models.CharField(max_length=100, choices=STATUS48, default="Urban")
    bstate = models.CharField(max_length=100, default="Maharashtra")
    bgstin = models.CharField(max_length=15, default="27")
    email = models.EmailField(max_length=60)
    STATUS9 = {
        ('New', 'New'),
        ('Existing', 'Existing'),
    }
    billaccno = models.CharField(max_length=20,choices=STATUS9,default="New")
    adharcardno = models.CharField(max_length=20,default="1",blank=True,null=True)
    adharcard = models.ImageField(upload_to='pics', default="profile1.png")
    panno = models.CharField(max_length=20,default="1", blank=True,null=True)
    pan = models.ImageField(upload_to='pics', default="profile1.png")
    drivinglicenceno = models.CharField(max_length=20,default="1",blank=True,null=True)
    drivinglicence = models.ImageField(upload_to='pics', default="profile1.png")
    electricityno = models.CharField(max_length=20,default="1",blank=True)
    electricitybill = models.ImageField(upload_to='pics', default="profile1.png")
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_id = models.IntegerField(null=True)
    STATUS10 = {
        ('BB Over Wifi', 'BB Over Wifi'),
        ('VPT', 'VPT'),
        ('MMVC PostPaid', 'MMVC PostPaid'),
        ('PT', 'PT'),
        ('Pubic Institution', 'Pubic Institution'),
        ('Retired BSNL Employee', 'Retired BSNL Employee'),
        ('Central Government', 'Central Government'),
        ('Foreign Embassy', 'Foreign Embassy'),
        ('Individual', 'Individual'),
        ('Public Utilities', 'Public Utilities'),
        ('Service', 'Service'),
        ('State Government', 'State Government'),
        ('Bharat Air Fibre', 'Bharat Air Fibre'),
    }
    accounttype = models.CharField(max_length=100, choices=STATUS10, default='Service')


    def __str__(self):
        return self.name



class Newcustomer9(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField()
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    uesrname = models.CharField(max_length=200, null=True)
    mobileno = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=60, null=True)
    adharcardno = models.CharField(max_length=20, null=True)
    adharcard = models.ImageField(upload_to='pics', default="profile1.png")
    panno = models.CharField(max_length=20, null=True)
    pan = models.ImageField(upload_to='pics', default="profile1.png")
    drivinglicenceno = models.CharField(max_length=20, null=True,default="1")
    drivinglicence = models.ImageField(upload_to='pics', default="profile1.png")
    electricityno = models.CharField(max_length=20, null=True)
    electricitybill = models.ImageField(upload_to='pics', default="profile1.png")
    active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    video = EmbedVideoField()


class Offer(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', default="profile1.png")
    desc = models.TextField()
    tempelate = models.CharField(max_length=100)

    def __str__(self):
        return 'Name:{0}   Description:{0} '.format(self.name, self.desc)


class Complain(models.Model):
    user1 = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=25, blank=False)
    accountno = models.CharField(max_length=25, blank=False)
    category = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True)
    date_solved = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField()


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', default="profile1.png")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Engineer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contactme(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.TextField()
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
    chairman = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    flats = models.IntegerField(default=6, null=True)
    oltip = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.building


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    benefits = models.CharField(max_length=150, blank=False)
    validity = models.CharField(max_length=150, blank=False)
    speedlimit = models.CharField(max_length=150, default=100, null=True)
    days = models.IntegerField(default=28, null=True)
    value = models.IntegerField()

    def __str__(self):
        return str(self.benefits)


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
    name = models.ForeignKey(Newcustomer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Plan, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = {
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Progress', 'Progress'),
        ('Installed', 'Installed'),
    }
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name),  str(self.status)


class My(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Progress', 'Progress'),
        ('Installed', 'Installed'),
    }
    name = models.ForeignKey(Newcustomer, null=True, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name,  self.status


class Installation(models.Model):
    name = models.ForeignKey(Newcustomer, null=True, on_delete=models.CASCADE)
    building = models.ForeignKey(Feasable, null=True, on_delete=models.CASCADE)
    flatno = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    voip = models.CharField(max_length=200, null=True, blank=True)
    userid = models.CharField(max_length=100, null=True, blank=True)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.CASCADE)
    ca = models.CharField(max_length=100, null=True, blank=True)
    ba = models.CharField(max_length=100, null=True, blank=True)
    ontmacid = models.CharField(max_length=100, null=True, blank=True)
    router = models.CharField(max_length=100, null=True, blank=True)
    dateapproval = models.DateTimeField(null=True, blank=True)
    timeapproval = models.TimeField(null=True, blank=True)
    dateococ = models.DateTimeField(null=True, blank=True)
    timeococ = models.TimeField(null=True, blank=True)
    dateinstalled = models.DateTimeField(null=True, blank=True)
    timeinstalled = models.TimeField(null=True, blank=True)
    datepayment = models.DateTimeField(null=True, blank=True)
    timepayment = models.TimeField(null=True, blank=True)
    datewo = models.DateTimeField(null=True, blank=True)
    timewo = models.TimeField(null=True, blank=True)
    rno = models.CharField(max_length=100, null=True, blank=True)
    mode = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    cablingby = models.CharField(max_length=100, null=True, blank=True)
    cablingdate = models.DateTimeField(null=True, blank=True)
    cablingtime = models.TimeField(null=True, blank=True)
    visitby = models.CharField(max_length=100, null=True, blank=True)
    visitdate = models.DateTimeField(null=True, blank=True)
    feedbackdate = models.DateTimeField(null=True, blank=True)
    isp = models.CharField(max_length=100, null=True, blank=True)
    marketing = models.CharField(max_length=100, null=True, blank=True)
    macid = models.CharField(max_length=100, null=True, blank=True)
    ontdetails = models.CharField(max_length=100, null=True, blank=True)
    ontsrno = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    STATUS = {
        ('InProgress', 'Inprogress'),
        ('Live', 'Live'),
        ('Disconnected', 'Disconnected'),
        ('Restored', 'Restored'),
        ('Suspended', 'Suspended'),
        ('Complain', 'Complain'),
    }
    status = models.CharField(max_length=100, null=True, blank=True,default="InProgress", choices=STATUS)

    def __str__(self):
        return self.name


class Installation2(models.Model):
    name = models.ForeignKey(Newcustomer, null=True, on_delete=models.CASCADE)
    building = models.ForeignKey(Feasable, null=True, on_delete=models.CASCADE)
    flatno = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    voip = models.CharField(max_length=200, null=True, blank=True)
    userid = models.CharField(max_length=100, null=True, blank=True)
    plan = models.ForeignKey(Plan, null=True, on_delete=models.CASCADE)
    ca = models.CharField(max_length=100, null=True, blank=True)
    ba = models.CharField(max_length=100, null=True, blank=True)
    ontmacid = models.CharField(max_length=100, null=True, blank=True)
    router = models.CharField(max_length=100, null=True, blank=True)
    dateapproval = models.DateTimeField(null=True, blank=True)
    timeapproval = models.TimeField(null=True, blank=True)
    dateococ = models.DateTimeField(null=True, blank=True)
    timeococ = models.TimeField(null=True, blank=True)
    dateinstalled = models.DateTimeField(null=True, blank=True)
    timeinstalled = models.TimeField(null=True, blank=True)
    datepayment = models.DateTimeField(null=True, blank=True)
    timepayment = models.TimeField(null=True, blank=True)
    datewo = models.DateTimeField(null=True, blank=True)
    timewo = models.TimeField(null=True, blank=True)
    rno = models.CharField(max_length=100, null=True, blank=True)
    mode = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    cablingby = models.CharField(max_length=100, null=True, blank=True)
    cablingdate = models.DateTimeField(null=True, blank=True)
    cablingtime = models.TimeField(null=True, blank=True)
    visitby = models.CharField(max_length=100, null=True, blank=True)
    visitdate = models.DateTimeField(null=True, blank=True)
    feedbackdate = models.DateTimeField(null=True, blank=True)
    isp = models.CharField(max_length=100, null=True, blank=True)
    marketing = models.CharField(max_length=100, null=True, blank=True)
    macid = models.CharField(max_length=100, null=True, blank=True)
    ontdetails = models.CharField(max_length=100, null=True, blank=True)
    ontsrno = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    STATUS = {
        ('InProgress', 'Inprogress'),
        ('Live', 'Live'),
        ('Disconnected', 'Disconnected'),
        ('Restored', 'Restored'),
        ('Suspended', 'Suspended'),
        ('Complain', 'Complain'),
    }
    status = models.CharField(max_length=100, null=True, blank=True, default="InProgress", choices=STATUS)

    def __str__(self):
        return self.name


class Newcustomer2(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, default="Pune")
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    STATUS2 = {
        ('MR', 'MR'),
        ('MS', 'MS'),
        ('MISS', 'MISS'),
        ('DR', 'DR'),
    }
    fathername = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True, choices=STATUS2)
    STATUS3 = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    }
    dob = models.DateTimeField(null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, default="India")
    gender = models.CharField(max_length=20, null=True, choices=STATUS3)
    STATUS4 = {
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
    }
    customertype = models.CharField(max_length=20, null=True, choices=STATUS4, default="Individual")
    STATUS5 = {
        ('Business', 'Business'),
        ('Residental', 'Residental'),
    }
    usage = models.CharField(max_length=20, null=True, choices=STATUS5, default="Residental")
    STATUS6 = {
        ('POSTPAID', 'POSTPAID'),
        ('PREPAID', 'PREPAID'),
    }
    connectiontype = models.CharField(max_length=20, null=True, choices=STATUS6, default="POSTPAID")
    STATUS7 = {
        ('Email', 'Email'),
        ('Mobile', 'Mobile'),
    }
    communicationmethod = models.CharField(max_length=20, null=True, choices=STATUS7, default="Email")
    accsubtype = models.CharField(max_length=100, null=True)
    STATUS20 = {
        ('Monthly', 'Monthly'),
        ('Bimonthly', 'Bimonthly'),
    }
    frequency = models.CharField(max_length=30, null=True, choices=STATUS20, default="Monthly")
    STATUS21 = {
        ('EMAIL', 'EMAIL'),
        ('Print Bill On Paper', 'Print Bill On Paper'),
        ('PAPER AND EMAIL', 'PAPER AND EMAIL'),
    }
    billmedia = models.CharField(max_length=20, null=True, choices=STATUS21, default="EMAIL")
    STATUS22 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card', 'Voter ID Card'),
        ('Goverment ID Card', 'Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card', 'PAN Card'),
        ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'),
        ('Passport', 'Passport'),
        ('Ration Card with Photo', 'Ration Card with Photo'),
        ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'),
    }
    poi = models.CharField(max_length=50, null=True, choices=STATUS22)
    poitype = models.CharField(max_length=100, null=True)
    poiref = models.CharField(max_length=100, null=True)
    STATUS23 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'),
        ('Income Tax Department', 'Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poiby = models.CharField(max_length=100, null=True, choices=STATUS23)
    poidate = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    STATUS32 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card', 'Voter ID Card'),
        ('Goverment ID Card', 'Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card', 'PAN Card'),
        ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'),
        ('Passport', 'Passport'),
        ('Ration Card with Photo', 'Ration Card with Photo'),
        ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'),
    }
    poa = models.CharField(max_length=50, null=True, choices=STATUS32)
    poatype = models.CharField(max_length=100, null=True)
    poaref = models.CharField(max_length=100, null=True)
    STATUS33 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'),
        ('Income Tax Department', 'Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poaby = models.CharField(max_length=100, null=True, choices=STATUS33)
    poadate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    billemail = models.CharField(max_length=20, null=True)
    uesrname = models.CharField(max_length=200, null=True, blank=True)
    mobileno = models.CharField(max_length=20, null=True, default="123")
    mobileno1 = models.CharField(max_length=20, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True)
    houseno = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, default="Pune")
    district = models.CharField(max_length=100, default="Pune")
    locaility = models.CharField(max_length=100, default="Pune")
    sublocaility = models.CharField(max_length=100, default="Pune")
    exchangecode = models.CharField(max_length=100, default="Pune")
    STATUS8 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    ccategory = models.CharField(max_length=100, choices=STATUS8, default="Urban")
    state = models.CharField(max_length=100, default="Maharashtra")
    gstin = models.CharField(max_length=15, default="27")

    bpincode = models.CharField(max_length=20, null=True, blank=True)
    bhouseno = models.CharField(max_length=100, null=True, blank=True)
    bvillage = models.CharField(max_length=100, null=True, blank=True)
    blandmark = models.CharField(max_length=100, null=True, blank=True)
    bcity = models.CharField(max_length=100, default="Pune", blank=True)
    baddress = models.CharField(max_length=500, default="Pune", blank=True)
    bdistrict = models.CharField(max_length=100, default="Pune", blank=True)
    blocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bsublocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bexchangecode = models.CharField(max_length=100, default="Pune", blank=True)
    STATUS48 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    bccategory = models.CharField(max_length=100, choices=STATUS48, default="Urban")
    bstate = models.CharField(max_length=100, default="Maharashtra")
    bgstin = models.CharField(max_length=15, default="27")
    email = models.EmailField(max_length=60)
    STATUS9 = {
        ('New', 'New'),
        ('Existing', 'Existing'),
    }
    billaccno = models.CharField(max_length=20, choices=STATUS9, default="New")
    adharcardno = models.CharField(max_length=20, default="1", blank=True, null=True)
    adharcard = models.ImageField(upload_to='pics', default="profile1.png")
    panno = models.CharField(max_length=20, default="1", blank=True, null=True)
    pan = models.ImageField(upload_to='pics', default="profile1.png")
    drivinglicenceno = models.CharField(max_length=20, default="1", blank=True, null=True)
    drivinglicence = models.ImageField(upload_to='pics', default="profile1.png")
    electricityno = models.CharField(max_length=20, default="1", blank=True)
    electricitybill = models.ImageField(upload_to='pics', default="profile1.png")
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_id = models.IntegerField(null=True)
    STATUS10 = {
        ('BB Over Wifi', 'BB Over Wifi'),
        ('VPT', 'VPT'),
        ('MMVC PostPaid', 'MMVC PostPaid'),
        ('PT', 'PT'),
        ('Pubic Institution', 'Pubic Institution'),
        ('Retired BSNL Employee', 'Retired BSNL Employee'),
        ('Central Government', 'Central Government'),
        ('Foreign Embassy', 'Foreign Embassy'),
        ('Individual', 'Individual'),
        ('Public Utilities', 'Public Utilities'),
        ('Service', 'Service'),
        ('State Government', 'State Government'),
        ('Bharat Air Fibre', 'Bharat Air Fibre'),
    }
    accounttype = models.CharField(max_length=100, choices=STATUS10, default='Service')

    def __str__(self):
        return self.name




class Newcustomer3(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, default="Pune")
    username = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    STATUS2 = {
        ('MR', 'MR'),
        ('MS', 'MS'),
        ('MISS', 'MISS'),
        ('DR', 'DR'),
    }
    fathername = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True, choices=STATUS2)
    STATUS3 = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    }
    dob = models.DateTimeField(null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, default="India")
    gender = models.CharField(max_length=20, null=True, choices=STATUS3)
    STATUS4 = {
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
    }
    customertype = models.CharField(max_length=20, null=True, choices=STATUS4, default="Individual")
    STATUS5 = {
        ('Business', 'Business'),
        ('Residental', 'Residental'),
    }
    usage = models.CharField(max_length=20, null=True, choices=STATUS5, default="Residental")
    STATUS6 = {
        ('POSTPAID', 'POSTPAID'),
        ('PREPAID', 'PREPAID'),
    }
    connectiontype = models.CharField(max_length=20, null=True, choices=STATUS6, default="POSTPAID")
    STATUS7 = {
        ('Email', 'Email'),
        ('Mobile', 'Mobile'),
    }
    communicationmethod = models.CharField(max_length=20, null=True, choices=STATUS7, default="Email")
    accsubtype = models.CharField(max_length=100, null=True)
    STATUS20 = {
        ('Monthly', 'Monthly'),
        ('Bimonthly', 'Bimonthly'),
    }
    frequency = models.CharField(max_length=30, null=True, choices=STATUS20, default="Monthly")
    STATUS21 = {
        ('EMAIL', 'EMAIL'),
        ('Print Bill On Paper', 'Print Bill On Paper'),
        ('PAPER AND EMAIL', 'PAPER AND EMAIL'),
    }
    billmedia = models.CharField(max_length=20, null=True, choices=STATUS21, default="EMAIL")
    STATUS22 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card', 'Voter ID Card'),
        ('Goverment ID Card', 'Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card', 'PAN Card'),
        ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'),
        ('Passport', 'Passport'),
        ('Ration Card with Photo', 'Ration Card with Photo'),
        ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'),
    }
    poi = models.CharField(max_length=50, null=True, choices=STATUS22)
    poitype = models.CharField(max_length=100, null=True)
    poiref = models.CharField(max_length=100, null=True)
    STATUS23 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'),
        ('Income Tax Department', 'Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poiby = models.CharField(max_length=100, null=True, choices=STATUS23)
    poidate = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    STATUS32 = {
        ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'),
        ('CGHS/EGHS Card', 'CGHS/EGHS Card'),
        ('Driving Licence', 'Driving Licence'),
        ('Voter ID Card', 'Voter ID Card'),
        ('Goverment ID Card', 'Goverment ID Card'),
        ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'),
        ('PAN Card', 'PAN Card'),
        ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'),
        ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'),
        ('Passport', 'Passport'),
        ('Ration Card with Photo', 'Ration Card with Photo'),
        ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'),
        ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'),
    }
    poa = models.CharField(max_length=50, null=True, choices=STATUS32)
    poatype = models.CharField(max_length=100, null=True)
    poaref = models.CharField(max_length=100, null=True)
    STATUS33 = {
        ('UIDAI Government Of India', 'UIDAI Government Of India'),
        ('The Central Govt Health Department', 'The Central Govt Health Department'),
        ('RTO', 'RTO'),
        ('ERO', 'ERO'),
        ('Government of India', 'Government of India'),
        ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'),
        ('Income Tax Department', 'Income Tax Department'),
        ('Village Panchayath', 'Village Panchayath'),
        ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'),
        ('Passport Authority', 'Passport Authority'),
        ('Ministry Of Defence', 'Ministry Of Defence'),
    }
    poaby = models.CharField(max_length=100, null=True, choices=STATUS33)
    poadate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    billemail = models.CharField(max_length=20, null=True)
    uesrname = models.CharField(max_length=200, null=True, blank=True)
    mobileno = models.CharField(max_length=20, null=True, default="123")
    mobileno1 = models.CharField(max_length=20, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True)
    houseno = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, default="Pune")
    district = models.CharField(max_length=100, default="Pune")
    locaility = models.CharField(max_length=100, default="Pune")
    sublocaility = models.CharField(max_length=100, default="Pune")
    exchangecode = models.CharField(max_length=100, default="Pune")
    STATUS8 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    ccategory = models.CharField(max_length=100, choices=STATUS8, default="Urban")
    state = models.CharField(max_length=100, default="Maharashtra")
    gstin = models.CharField(max_length=15, default="27")

    bpincode = models.CharField(max_length=20, null=True, blank=True)
    bhouseno = models.CharField(max_length=100, null=True, blank=True)
    bvillage = models.CharField(max_length=100, null=True, blank=True)
    blandmark = models.CharField(max_length=100, null=True, blank=True)
    bcity = models.CharField(max_length=100, default="Pune", blank=True)
    baddress = models.CharField(max_length=500, default="Pune", blank=True)
    bdistrict = models.CharField(max_length=100, default="Pune", blank=True)
    blocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bsublocaility = models.CharField(max_length=100, default="Pune", blank=True)
    bexchangecode = models.CharField(max_length=100, default="Pune", blank=True)
    STATUS48 = {
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
    }
    bccategory = models.CharField(max_length=100, choices=STATUS48, default="Urban")
    bstate = models.CharField(max_length=100, default="Maharashtra")
    bgstin = models.CharField(max_length=15, default="27")
    email = models.EmailField(max_length=60)
    STATUS9 = {
        ('New', 'New'),
        ('Existing', 'Existing'),
    }
    billaccno = models.CharField(max_length=20, choices=STATUS9, default="New")
    adharcardno = models.CharField(max_length=20, default="1", blank=True, null=True)
    adharcard = models.ImageField(upload_to='pics', default="profile1.png")
    panno = models.CharField(max_length=20, default="1", blank=True, null=True)
    pan = models.ImageField(upload_to='pics', default="profile1.png")
    drivinglicenceno = models.CharField(max_length=20, default="1", blank=True, null=True)
    drivinglicence = models.ImageField(upload_to='pics', default="profile1.png")
    electricityno = models.CharField(max_length=20, default="1", blank=True)
    electricitybill = models.ImageField(upload_to='pics', default="profile1.png")
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_id = models.IntegerField(null=True)
    STATUS10 = {
        ('BB Over Wifi', 'BB Over Wifi'),
        ('VPT', 'VPT'),
        ('MMVC PostPaid', 'MMVC PostPaid'),
        ('PT', 'PT'),
        ('Pubic Institution', 'Pubic Institution'),
        ('Retired BSNL Employee', 'Retired BSNL Employee'),
        ('Central Government', 'Central Government'),
        ('Foreign Embassy', 'Foreign Embassy'),
        ('Individual', 'Individual'),
        ('Public Utilities', 'Public Utilities'),
        ('Service', 'Service'),
        ('State Government', 'State Government'),
        ('Bharat Air Fibre', 'Bharat Air Fibre'),
    }
    accounttype = models.CharField(max_length=100, choices=STATUS10, default='Service')

    def __str__(self):
        return self.name
