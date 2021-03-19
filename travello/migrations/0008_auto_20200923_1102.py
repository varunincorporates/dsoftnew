# Generated by Django 3.0.6 on 2020-09-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0007_auto_20200923_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='time1installed',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('OnContract', 'OnContract'), ('Working', 'Working'), ('Resigned', 'Resigned'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('OnContract', 'OnContract'), ('Working', 'Working'), ('Resigned', 'Resigned'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='installation',
            name='status',
            field=models.CharField(blank=True, choices=[('Disconnected', 'Disconnected'), ('Complain', 'Complain'), ('Live', 'Live'), ('Suspended', 'Suspended'), ('Restored', 'Restored'), ('InProgress', 'Inprogress')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='installation2',
            name='status',
            field=models.CharField(blank=True, choices=[('Disconnected', 'Disconnected'), ('Complain', 'Complain'), ('Live', 'Live'), ('Suspended', 'Suspended'), ('Restored', 'Restored'), ('InProgress', 'Inprogress')], default='InProgress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='my',
            name='status',
            field=models.CharField(choices=[('Progress', 'Progress'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Progress', 'Progress'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('INPROGESS', 'INPROGRESS'), ('OPEN', 'OPEN'), ('RESOLVED', 'RESOLVED')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('SOLVED', 'SOLVED'), ('VISIT', 'VISIT'), ('PENDING', 'PENDING'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='accounttype',
            field=models.CharField(choices=[('VPT', 'VPT'), ('Individual', 'Individual'), ('Public Utilities', 'Public Utilities'), ('PT', 'PT'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('State Government', 'State Government'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('Central Government', 'Central Government'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='billaccno',
            field=models.CharField(choices=[('New', 'New'), ('Existing', 'Existing')], default='New', max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='billmedia',
            field=models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='connectiontype',
            field=models.CharField(choices=[('PREPAID', 'PREPAID'), ('POSTPAID', 'POSTPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='frequency',
            field=models.CharField(choices=[('Bimonthly', 'Bimonthly'), ('Monthly', 'Monthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='lastname',
            field=models.CharField(choices=[('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poa',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poaby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poi',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='poiby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='accounttype',
            field=models.CharField(choices=[('VPT', 'VPT'), ('Individual', 'Individual'), ('Public Utilities', 'Public Utilities'), ('PT', 'PT'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('State Government', 'State Government'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('Central Government', 'Central Government'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='billaccno',
            field=models.CharField(choices=[('New', 'New'), ('Existing', 'Existing')], default='New', max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='billmedia',
            field=models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='connectiontype',
            field=models.CharField(choices=[('PREPAID', 'PREPAID'), ('POSTPAID', 'POSTPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='frequency',
            field=models.CharField(choices=[('Bimonthly', 'Bimonthly'), ('Monthly', 'Monthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='lastname',
            field=models.CharField(choices=[('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poa',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poaby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poi',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='poiby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer2',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='accounttype',
            field=models.CharField(choices=[('VPT', 'VPT'), ('Individual', 'Individual'), ('Public Utilities', 'Public Utilities'), ('PT', 'PT'), ('MMVC PostPaid', 'MMVC PostPaid'), ('BB Over Wifi', 'BB Over Wifi'), ('State Government', 'State Government'), ('Bharat Air Fibre', 'Bharat Air Fibre'), ('Retired BSNL Employee', 'Retired BSNL Employee'), ('Service', 'Service'), ('Foreign Embassy', 'Foreign Embassy'), ('Central Government', 'Central Government'), ('Pubic Institution', 'Pubic Institution')], default='Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='billaccno',
            field=models.CharField(choices=[('New', 'New'), ('Existing', 'Existing')], default='New', max_length=20),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='billmedia',
            field=models.CharField(choices=[('PAPER AND EMAIL', 'PAPER AND EMAIL'), ('EMAIL', 'EMAIL'), ('Print Bill On Paper', 'Print Bill On Paper')], default='EMAIL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='connectiontype',
            field=models.CharField(choices=[('PREPAID', 'PREPAID'), ('POSTPAID', 'POSTPAID')], default='POSTPAID', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='customertype',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual')], default='Individual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='frequency',
            field=models.CharField(choices=[('Bimonthly', 'Bimonthly'), ('Monthly', 'Monthly')], default='Monthly', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='lastname',
            field=models.CharField(choices=[('DR', 'DR'), ('MR', 'MR'), ('MS', 'MS'), ('MISS', 'MISS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poa',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poaby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poi',
            field=models.CharField(choices=[('Ration Card with Photo', 'Ration Card with Photo'), ('Voter ID Card', 'Voter ID Card'), ('CGHS/EGHS Card', 'CGHS/EGHS Card'), ('Goverment ID Card', 'Goverment ID Card'), ('Unique Indentificationby Authority Of India', 'Unique Indentificationby Authority Of India'), ('Passport', 'Passport'), ('Smart Card by CSD Defence', 'Smart Card by CSD Defence'), ('Pass Book Of Bank or PO', 'Pass Book Of Bank or PO'), ('Photo ID Card by Edu Institute', 'Photo ID Card by Edu Institute'), ('Photo ID by Village Panchayath', 'Photo ID by Village Panchayath'), ('Driving Licence', 'Driving Licence'), ('Certificate Issued By MLA MP GR A Officer', 'Certificate Issued By MLA MP GR A Officer'), ('PAN Card', 'PAN Card')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='poiby',
            field=models.CharField(choices=[('The Central Govt Health Department', 'The Central Govt Health Department'), ('ERO', 'ERO'), ('RTO', 'RTO'), ('Income Tax Department', 'Income Tax Department'), ('Issued By MLA MP GR A Officer', 'Issued By MLA MP GR A Officer'), ('Bank Branch Manager or PO', 'Pass Book Of Bank or PO'), ('UIDAI Government Of India', 'UIDAI Government Of India'), ('Village Panchayath', 'Village Panchayath'), ('Ministry Of Defence', 'Ministry Of Defence'), ('Government of India', 'Government of India'), ('Passport Authority', 'Passport Authority')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer3',
            name='usage',
            field=models.CharField(choices=[('Residental', 'Residental'), ('Business', 'Business')], default='Residental', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]