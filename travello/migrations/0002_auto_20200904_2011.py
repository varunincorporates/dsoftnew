# Generated by Django 3.0.6 on 2020-09-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('OnContract', 'OnContract'), ('Working', 'Working'), ('Temporary', 'Temporary'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('OnContract', 'OnContract'), ('Working', 'Working'), ('Temporary', 'Temporary'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Pending', 'Pending'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]