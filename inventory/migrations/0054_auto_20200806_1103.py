# Generated by Django 3.0.6 on 2020-08-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0053_auto_20200806_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('B', 'Medium value items'), ('C', 'Low Value items'), ('A', 'high value items')], default='B', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('S', 'slow moving items'), ('F', 'fast moving items'), ('M', 'medium moving items')], default='M', max_length=1),
        ),
    ]
