# Generated by Django 3.0.6 on 2020-08-24 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travello', '0003_auto_20200824_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee1',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Installed', 'Installed'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('PENDING', 'PENDING'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('BILL DISPUTE', 'BILL DISPUTE'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Billing Complant', 'Billing Complant'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('PENDING', 'PENDING'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('BILL DISPUTE', 'BILL DISPUTE'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
