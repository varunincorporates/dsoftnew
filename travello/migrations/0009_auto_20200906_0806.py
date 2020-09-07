# Generated by Django 3.0.6 on 2020-09-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0008_auto_20200906_0801'),
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
            field=models.CharField(choices=[('Pending', 'Pending'), ('Progress', 'Progress'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('OPEN', 'OPEN'), ('INPROGESS', 'INPROGRESS')], default='OPEN', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('VISIT', 'VISIT')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('CABLE CUT', 'CABLE CUT')], max_length=200, null=True),
        ),
    ]