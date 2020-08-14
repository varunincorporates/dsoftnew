# Generated by Django 3.0.5 on 2020-08-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_auto_20200809_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcomplain',
            name='comments',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Progress', 'Progress'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Relocation', 'Relocation'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]