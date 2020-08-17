# Generated by Django 3.0.6 on 2020-08-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_auto_20200817_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Working', 'Working'), ('Temporary', 'Temporary'), ('OnContract', 'OnContract'), ('Resigned', 'Resigned')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Installed', 'Installed'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Progress', 'Progress')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('VISIT', 'VISIT'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('No Connection', 'No Connection'), ('Slow Speed', 'Slow Speed'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('N.A.', 'N.A.'), ('SOLVED', 'SOLVED'), ('VISIT', 'VISIT'), ('OBSERVATION', 'OBSERVATION'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('CABLE CUT', 'CABLE CUT'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('BILL DISPUTE', 'BILL DISPUTE'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED')], max_length=200, null=True),
        ),
    ]
