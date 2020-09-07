# Generated by Django 3.0.6 on 2020-09-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0010_auto_20200906_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Progress', 'Progress'), ('Installed', 'Installed'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('INPROGESS', 'INPROGRESS'), ('RESOLVED', 'RESOLVED')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED'), ('PENDING', 'PENDING'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('BILL DISPUTE', 'BILL DISPUTE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]