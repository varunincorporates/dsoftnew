# Generated by Django 3.0.5 on 2020-07-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20200728_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='status',
            field=models.CharField(choices=[('Reg', 'Registered'), ('Pend', 'Pending'), ('NA', 'not applicable'), ('Progress', 'In Process'), ('OK', 'OK'), ('NOC', 'No Coverage')], default='Reg', max_length=10),
        ),
    ]
