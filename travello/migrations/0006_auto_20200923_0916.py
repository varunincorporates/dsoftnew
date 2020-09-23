# Generated by Django 3.0.6 on 2020-09-23 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20200922_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='time1approval',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='installation',
            name='status',
            field=models.CharField(blank=True, choices=[('Complain', 'Complain'), ('InProgress', 'Inprogress'), ('Live', 'Live'), ('Suspended', 'Suspended'), ('Restored', 'Restored'), ('Disconnected', 'Disconnected')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='installation2',
            name='status',
            field=models.CharField(blank=True, choices=[('Complain', 'Complain'), ('InProgress', 'Inprogress'), ('Live', 'Live'), ('Suspended', 'Suspended'), ('Restored', 'Restored'), ('Disconnected', 'Disconnected')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='my',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Installed', 'Installed'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Installed', 'Installed'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('OPEN', 'OPEN'), ('INPROGESS', 'INPROGRESS')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('OBSERVATION', 'OBSERVATION'), ('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('VISIT', 'VISIT'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='accounttype',
            field=models.CharField(choices=[('Bharat Air Fibre', 'Bharat Air Fibre'), ('VPT', 'VPT'), ('Pubic Institution', 'Pubic Institution'), ('Public Utilities', 'Public Utilities'), ('State Government', 'State Government'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('BB Over Wifi', 'BB Over Wifi'), ('Central Government', 'Central Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('PT', 'PT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Individual', 'Individual')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='billmedia',
            field=models.CharField(choices=[('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper'), ('PAPER AND EMAIL', 'PAPER AND EMAIL')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='communicationmethod',
            field=models.CharField(choices=[('Email', 'Email'), ('Mobile', 'Mobile')], default='Email', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='connectiontype',
            field=models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
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
            field=models.CharField(choices=[('MS', 'MS'), ('DR', 'DR'), ('MR', 'MR'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poa',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poaby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poi',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poiby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='accounttype',
            field=models.CharField(choices=[('Bharat Air Fibre', 'Bharat Air Fibre'), ('VPT', 'VPT'), ('Pubic Institution', 'Pubic Institution'), ('Public Utilities', 'Public Utilities'), ('State Government', 'State Government'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('BB Over Wifi', 'BB Over Wifi'), ('Central Government', 'Central Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('PT', 'PT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Individual', 'Individual')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='billmedia',
            field=models.CharField(choices=[('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper'), ('PAPER AND EMAIL', 'PAPER AND EMAIL')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='communicationmethod',
            field=models.CharField(choices=[('Email', 'Email'), ('Mobile', 'Mobile')], default='Email', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='connectiontype',
            field=models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='frequency',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Bimonthly', 'Bimonthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='lastname',
            field=models.CharField(choices=[('MS', 'MS'), ('DR', 'DR'), ('MR', 'MR'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poa',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poaby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poi',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poiby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='accounttype',
            field=models.CharField(choices=[('Bharat Air Fibre', 'Bharat Air Fibre'), ('VPT', 'VPT'), ('Pubic Institution', 'Pubic Institution'), ('Public Utilities', 'Public Utilities'), ('State Government', 'State Government'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('BB Over Wifi', 'BB Over Wifi'), ('Central Government', 'Central Government'), ('MMVC PostPaid', 'MMVC PostPaid'), ('PT', 'PT'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Individual', 'Individual')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='billmedia',
            field=models.CharField(choices=[('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper'), ('PAPER AND EMAIL', 'PAPER AND EMAIL')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='communicationmethod',
            field=models.CharField(choices=[('Email', 'Email'), ('Mobile', 'Mobile')], default='Email', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='connectiontype',
            field=models.CharField(choices=[('POSTPAID', 'POSTPAID'), ('PREPAID', 'PREPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='frequency',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Bimonthly', 'Bimonthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='lastname',
            field=models.CharField(choices=[('MS', 'MS'), ('DR', 'DR'), ('MR', 'MR'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poa',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poaby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poi',
            field=models.CharField(choices=[('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('PAN Card', 'PAN Card'), ('Passport', 'Passport'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Voter ID Card', 'Voter ID Card'), ('Ration Card with Photo', 'Ration Card with Photo'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Driving Licence', 'Driving Licence'), ('Goverment ID Card', 'Goverment ID Card'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('CGHS/EGHS Card', 'CGHS/EGHS Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poiby',
            field=models.CharField(choices=[('Ministry Of Defence', 'Ministry Of Defence'), ('Passport Authority', 'Passport Authority'), ('RTO', 'RTO'), ('Village Panchayath', 'Village Panchayath'), ('Income Tax Department', 'Income Tax Department'), ('Government of India', 'Government of India'), ('ERO', 'ERO'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('The Central Govt Health Department', 'The Central Govt Health Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
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
            field=models.CharField(choices=[('Working', 'Working'), ('Suspended', 'Suspended'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract')], max_length=200, null=True),
        ),
    ]
