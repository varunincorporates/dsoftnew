# Generated by Django 3.0.6 on 2020-08-17 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_reg1', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Working', 'Working'), ('Resigned', 'Resigned'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feasable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='Newcustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('address', models.TextField()),
                ('mobileno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('adharcardno', models.CharField(max_length=20)),
                ('adharcard', models.ImageField(upload_to='pics')),
                ('panno', models.CharField(max_length=20)),
                ('pan', models.ImageField(upload_to='pics')),
                ('drivinglicenceno', models.CharField(max_length=20)),
                ('drivinglicence', models.ImageField(upload_to='pics')),
                ('electricityno', models.CharField(max_length=20)),
                ('electricitybill', models.ImageField(upload_to='pics')),
                ('active', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('tempelate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefits', models.CharField(max_length=150)),
                ('validity', models.CharField(max_length=150)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Referal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=50)),
                ('mymobile', models.CharField(max_length=20)),
                ('referalname', models.CharField(max_length=50)),
                ('referalmobile', models.CharField(max_length=20)),
                ('referalemail', models.EmailField(max_length=60)),
                ('referaladdress', models.TextField()),
                ('message', models.TextField()),
                ('category', models.CharField(max_length=25)),
                ('contacttime', models.CharField(max_length=30)),
                ('date_reg1', models.DateTimeField(auto_now_add=True, verbose_name='date_reg1')),
            ],
        ),
        migrations.CreateModel(
            name='Salesfaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=25)),
                ('serial', models.IntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newcomplain1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=60)),
                ('accountno', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection')], max_length=200, null=True)),
                ('subject', models.CharField(choices=[('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True)),
                ('note', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('VISIT', 'VISIT'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True)),
                ('date_solved', models.DateTimeField(auto_now=True, null=True)),
                ('comments', models.TextField(null=True)),
                ('user1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Newcomplain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=60)),
                ('accountno', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection')], max_length=200, null=True)),
                ('subject', models.CharField(choices=[('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('BILL DISPUTE', 'BILL DISPUTE'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING')], max_length=200, null=True)),
                ('note', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('VISIT', 'VISIT'), ('SOLVED', 'SOLVED'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING'), ('N.A.', 'N.A.')], default='PENDING', max_length=200, null=True)),
                ('date_solved', models.DateTimeField(auto_now=True, null=True)),
                ('comments', models.TextField(null=True)),
                ('user1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Myorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Installed', 'Installed'), ('Progress', 'Progress')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.Newcustomer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='travello.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('accountno', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('date_solved', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.TextField()),
                ('user1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
