# Generated by Django 3.0.6 on 2020-08-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0075_auto_20200806_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('A', 'high value items'), ('B', 'Medium value items'), ('C', 'Low Value items')], default='B', max_length=10),
        ),
    ]
