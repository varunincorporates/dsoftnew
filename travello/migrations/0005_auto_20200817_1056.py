# Generated by Django 3.0.6 on 2020-08-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200817_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Resigned', 'Resigned'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Resigned', 'Resigned'), ('Working', 'Working'), ('OnContract', 'OnContract'), ('Temporary', 'Temporary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Installed', 'Installed'), ('Pending', 'Pending'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('PENDING', 'PENDING'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Billing Complant', 'Billing Complant'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Relocation', 'Relocation')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('PENDING', 'PENDING'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]
