# Generated by Django 3.0.6 on 2020-09-06 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_auto_20200906_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract'), ('Working', 'Working')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract'), ('Working', 'Working')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('INPROGESS', 'INPROGRESS'), ('RESOLVED', 'RESOLVED'), ('OPEN', 'OPEN')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('VISIT', 'VISIT'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
    ]