# Generated by Django 3.0.6 on 2020-08-24 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travello', '0002_auto_20200824_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('CABLE CUT', 'CABLE CUT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
