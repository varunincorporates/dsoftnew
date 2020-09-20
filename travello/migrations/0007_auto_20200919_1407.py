# Generated by Django 3.0.6 on 2020-09-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_auto_20200919_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='timewo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Progress', 'Progress'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('INPROGESS', 'INPROGRESS'), ('OPEN', 'OPEN')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('N.A.', 'N.A.'), ('PENDING', 'PENDING'), ('VISIT', 'VISIT')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='accounttype',
            field=models.CharField(choices=[('Bharat Air Fibre', 'Bharat Air Fibre'), ('Individual', 'Individual'), ('Public Utilities', 'Public Utilities'), ('Service', 'Service'), ('BB Over Wifi', 'BB Over Wifi'), ('State Government', 'State Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('Pubic Institution', 'Pubic Institution'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('PT', 'PT'), ('Foreign Embassy', 'Foreign Embassy'), ('VPT', 'VPT'), ('Central Government', 'Central Government')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='bccategory',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], default='Urban', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='billmedia',
            field=models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper'), ('EMAIL', 'EMAIL')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='ccategory',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')], default='Urban', max_length=100),
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
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='lastname',
            field=models.CharField(choices=[('DR', 'DR'), ('MISS', 'MISS'), ('MR', 'MR'), ('MS', 'MS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poa',
            field=models.CharField(choices=[('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Ration Card with Photo', 'Ration Card with Photo'), ('PAN Card', 'PAN Card'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Passport', 'Passport'), ('Goverment ID Card', 'Goverment ID Card'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Driving Licence', 'Driving Licence'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poaby',
            field=models.CharField(choices=[('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('ERO', 'ERO'), ('Passport Authority', 'Passport Authority'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('Village Panchayath', 'Village Panchayath'), ('RTO', 'RTO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poi',
            field=models.CharField(choices=[('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Ration Card with Photo', 'Ration Card with Photo'), ('PAN Card', 'PAN Card'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Passport', 'Passport'), ('Goverment ID Card', 'Goverment ID Card'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Driving Licence', 'Driving Licence'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poiby',
            field=models.CharField(choices=[('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('ERO', 'ERO'), ('Passport Authority', 'Passport Authority'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('Village Panchayath', 'Village Panchayath'), ('RTO', 'RTO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
