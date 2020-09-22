# Generated by Django 3.0.6 on 2020-09-20 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travello', '0002_auto_20200921_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='installation',
            name='status',
            field=models.CharField(blank=True, choices=[('Suspended', 'Suspended'), ('InProgress', 'Inprogress'), ('Restored', 'Restored'), ('Disconnected', 'Disconnected'), ('Live', 'Live'), ('Complain', 'Complain')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='installation2',
            name='status',
            field=models.CharField(blank=True, choices=[('Suspended', 'Suspended'), ('InProgress', 'Inprogress'), ('Restored', 'Restored'), ('Disconnected', 'Disconnected'), ('Live', 'Live'), ('Complain', 'Complain')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='my',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('INPROGESS', 'INPROGRESS'), ('OPEN', 'OPEN')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('SOLVED', 'SOLVED'), ('PENDING', 'PENDING'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='accounttype',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Service', 'Service'), ('Central Government', 'Central Government'), ('Public Utilities', 'Public Utilities'), ('Foreign Embassy', 'Foreign Embassy'), ('VPT', 'VPT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('State Government', 'State Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('PT', 'PT'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='connectiontype',
            field=models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customertype',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Corporate', 'Corporate')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='frequency',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Bimonthly', 'Bimonthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='lastname',
            field=models.CharField(choices=[('MISS', 'MISS'), ('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poa',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poaby',
            field=models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poi',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poiby',
            field=models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='accounttype',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Service', 'Service'), ('Central Government', 'Central Government'), ('Public Utilities', 'Public Utilities'), ('Foreign Embassy', 'Foreign Embassy'), ('VPT', 'VPT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('State Government', 'State Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('PT', 'PT'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='connectiontype',
            field=models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='customertype',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Corporate', 'Corporate')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='frequency',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Bimonthly', 'Bimonthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='lastname',
            field=models.CharField(choices=[('MISS', 'MISS'), ('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poa',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poaby',
            field=models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poi',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poiby',
            field=models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('Temporary', 'Temporary'), ('Working', 'Working'), ('Suspended', 'Suspended'), ('OnContract', 'OnContract')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Newcustomer3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(default='Pune', max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('fathername', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(choices=[('MISS', 'MISS'), ('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS')], max_length=200, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('nationality', models.CharField(default='India', max_length=20, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True)),
                ('customertype', models.CharField(choices=[('Individual', 'Individual'), ('Corporate', 'Corporate')], default='Individual', max_length=20, null=True)),
                ('usage', models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True)),
                ('connectiontype', models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True)),
                ('communicationmethod', models.CharField(choices=[('Mobile', 'Mobile'), ('Email', 'Email')], default='Email', max_length=20, null=True)),
                ('accsubtype', models.CharField(max_length=100, null=True)),
                ('frequency', models.CharField(choices=[('Monthly', 'Monthly'), ('Bimonthly', 'Bimonthly')], default='Monthly', max_length=30, null=True)),
                ('billmedia', models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper')], default='EMAIL', max_length=20, null=True)),
                ('poi', models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True)),
                ('poitype', models.CharField(max_length=100, null=True)),
                ('poiref', models.CharField(max_length=100, null=True)),
                ('poiby', models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True)),
                ('poidate', models.DateTimeField(blank=True, null=True)),
                ('poa', models.CharField(choices=[('PAN Card', 'PAN Card'), ('Voter ID Card', 'Voter ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Passport', 'Passport'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Goverment ID Card', 'Goverment ID Card')], max_length=50, null=True)),
                ('poatype', models.CharField(max_length=100, null=True)),
                ('poaref', models.CharField(max_length=100, null=True)),
                ('poaby', models.CharField(choices=[('Passport Authority', 'Passport Authority'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Government of India', 'Government of India'), ('ERO', 'ERO')], max_length=100, null=True)),
                ('poadate', models.DateTimeField(blank=True, null=True)),
                ('billemail', models.CharField(max_length=20, null=True)),
                ('uesrname', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileno', models.CharField(default='123', max_length=20, null=True)),
                ('mobileno1', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('houseno', models.CharField(max_length=100, null=True)),
                ('village', models.CharField(max_length=100, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(default='Pune', max_length=100)),
                ('district', models.CharField(default='Pune', max_length=100)),
                ('locaility', models.CharField(default='Pune', max_length=100)),
                ('sublocaility', models.CharField(default='Pune', max_length=100)),
                ('exchangecode', models.CharField(default='Pune', max_length=100)),
                ('ccategory', models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], default='Urban', max_length=100)),
                ('state', models.CharField(default='Maharashtra', max_length=100)),
                ('gstin', models.CharField(default='27', max_length=15)),
                ('bpincode', models.CharField(blank=True, max_length=20, null=True)),
                ('bhouseno', models.CharField(blank=True, max_length=100, null=True)),
                ('bvillage', models.CharField(blank=True, max_length=100, null=True)),
                ('blandmark', models.CharField(blank=True, max_length=100, null=True)),
                ('bcity', models.CharField(blank=True, default='Pune', max_length=100)),
                ('baddress', models.CharField(blank=True, default='Pune', max_length=500)),
                ('bdistrict', models.CharField(blank=True, default='Pune', max_length=100)),
                ('blocaility', models.CharField(blank=True, default='Pune', max_length=100)),
                ('bsublocaility', models.CharField(blank=True, default='Pune', max_length=100)),
                ('bexchangecode', models.CharField(blank=True, default='Pune', max_length=100)),
                ('bccategory', models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], default='Urban', max_length=100)),
                ('bstate', models.CharField(default='Maharashtra', max_length=100)),
                ('bgstin', models.CharField(default='27', max_length=15)),
                ('email', models.EmailField(max_length=60)),
                ('billaccno', models.CharField(choices=[('New', 'New'), ('Existing', 'Existing')], default='New', max_length=20)),
                ('adharcardno', models.CharField(blank=True, default='1', max_length=20, null=True)),
                ('adharcard', models.ImageField(default='profile1.png', upload_to='pics')),
                ('panno', models.CharField(blank=True, default='1', max_length=20, null=True)),
                ('pan', models.ImageField(default='profile1.png', upload_to='pics')),
                ('drivinglicenceno', models.CharField(blank=True, default='1', max_length=20, null=True)),
                ('drivinglicence', models.ImageField(default='profile1.png', upload_to='pics')),
                ('electricityno', models.CharField(blank=True, default='1', max_length=20)),
                ('electricitybill', models.ImageField(default='profile1.png', upload_to='pics')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_id', models.IntegerField(null=True)),
                ('accounttype', models.CharField(choices=[('Individual', 'Individual'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Service', 'Service'), ('Central Government', 'Central Government'), ('Public Utilities', 'Public Utilities'), ('Foreign Embassy', 'Foreign Embassy'), ('VPT', 'VPT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('State Government', 'State Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('PT', 'PT'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]