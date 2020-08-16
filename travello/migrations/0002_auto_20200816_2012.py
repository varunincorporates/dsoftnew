# Generated by Django 3.0.6 on 2020-08-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Progress', 'Progress'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Relocation', 'Relocation'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('CABLE CUT', 'CABLE CUT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
    ]
