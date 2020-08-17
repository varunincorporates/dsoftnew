# Generated by Django 3.0.6 on 2020-08-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20200817_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Installed', 'Installed'), ('Progress', 'Progress'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('VISIT', 'VISIT'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('VISIT', 'VISIT'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
    ]
