# Generated by Django 3.0.6 on 2020-08-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0191_auto_20200824_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('A', 'high value items'), ('C', 'Low Value items'), ('B', 'Medium value items')], default='B', max_length=10),
        ),
    ]
