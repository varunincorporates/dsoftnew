# Generated by Django 3.0.6 on 2020-08-17 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20200817_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='days',
            field=models.IntegerField(default=28, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='speedlimit',
            field=models.CharField(default=100, max_length=150, null=True),
        ),
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
            field=models.CharField(choices=[('Progress', 'Progress'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Installed', 'Installed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain',
            name='subject',
            field=models.CharField(choices=[('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('BILL DISPUTE', 'BILL DISPUTE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='category',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('Slow Speed', 'Slow Speed'), ('No Connection', 'No Connection'), ('Billing Complant', 'Billing Complant')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='status',
            field=models.CharField(choices=[('VISIT', 'VISIT'), ('N.A.', 'N.A.'), ('OBSERVATION', 'OBSERVATION'), ('SOLVED', 'SOLVED'), ('PENDING', 'PENDING')], default='PENDING', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='newcomplain1',
            name='subject',
            field=models.CharField(choices=[('PASSWORD FORGOT', 'PASSWORD FORGOT'), ('PAYMENT PROBLEM', 'PAYMENT PROBLEM'), ('SLOW SPEED TEST', 'SLOW SPEED TEST'), ('EQUIPEMENT PROBLEM', 'EQUIPEMENT PROBLEM'), ('WEBSITE NOT OPENING', 'WEBSITE NOT OPENING'), ('CABLE CUT', 'CABLE CUT'), ('ROUTER SUPPORT', 'ROUTER SUPPORT'), ('PAYMENT NOT UPDATED', 'PAYMENT NOT UPDATED'), ('BILL DISPUTE', 'BILL DISPUTE'), ('FREQUENTLY DISCONNECT', 'FREQUENTLY DISCONNECT'), ('UNABLE TO BROWSE', 'UNABLE TO BROWSE')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flatno', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('voip', models.CharField(max_length=200, null=True)),
                ('userid', models.CharField(max_length=100, null=True)),
                ('ca', models.CharField(max_length=100, null=True)),
                ('ba', models.CharField(max_length=100, null=True)),
                ('ontmacid', models.CharField(max_length=100, null=True)),
                ('router', models.CharField(max_length=100, null=True)),
                ('dateinstalled', models.DateTimeField(null=True)),
                ('rno', models.CharField(max_length=100, null=True)),
                ('mode', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('cablingby', models.CharField(max_length=100, null=True)),
                ('cablingdate', models.DateTimeField(null=True)),
                ('visitdate', models.DateTimeField(null=True)),
                ('isp', models.CharField(max_length=100, null=True)),
                ('marketing', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.Feasable')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.Newcustomer')),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.Plan')),
                ('visitby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travello.Employee')),
            ],
        ),
    ]
