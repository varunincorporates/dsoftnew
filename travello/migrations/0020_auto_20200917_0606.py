# Generated by Django 3.0.6 on 2020-09-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0019_auto_20200917_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('OnContract', 'OnContract'), ('Working', 'Working'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('OnContract', 'OnContract'), ('Working', 'Working'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Installed', 'Installed'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('INPROGESS', 'INPROGRESS'), ('RESOLVED', 'RESOLVED'), ('OPEN', 'OPEN')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('BILL DISPUTE', 'BILL DISPUTE'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('SOLVED', 'SOLVED'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('VISIT', 'VISIT'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('BILL DISPUTE', 'BILL DISPUTE'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='accounttype',
            field=models.CharField(choices=[('State Government', 'State Government'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('VPT', 'VPT'), ('MMVC PostPaid', 'MMVC PostPaid'), ('Individual', 'Individual'), ('Central Government', 'Central Government'), ('Foreign Embassy', 'Foreign Embassy'), ('Service', 'Service'), ('BB Over Wifi', 'BB Over Wifi'), ('PT', 'PT'), ('Pubic Institution', 'Pubic Institution'), ('Public Utilities', 'Public Utilities')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='billmedia',
            field=models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Other', 'Other'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='lastname',
            field=models.CharField(choices=[('MISS', 'MISS'), ('DR', 'DR'), ('MS', 'MS'), ('MR', 'MR')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poa',
            field=models.CharField(choices=[('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Goverment ID Card', 'Goverment ID Card'), ('Voter ID Card', 'Voter ID Card'), ('Passport', 'Passport'), ('PAN Card', 'PAN Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poaby',
            field=models.CharField(choices=[('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Village Panchayath', 'Village Panchayath'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Income Tax Department', 'Income Tax Department'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Passport Authority', 'Passport Authority'), ('Government of India', 'Government of India'), ('Ministry Of Defence', 'Ministry Of Defence')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poi',
            field=models.CharField(choices=[('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Goverment ID Card', 'Goverment ID Card'), ('Voter ID Card', 'Voter ID Card'), ('Passport', 'Passport'), ('PAN Card', 'PAN Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poiby',
            field=models.CharField(choices=[('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Village Panchayath', 'Village Panchayath'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('Income Tax Department', 'Income Tax Department'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Passport Authority', 'Passport Authority'), ('Government of India', 'Government of India'), ('Ministry Of Defence', 'Ministry Of Defence')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]
