# Generated by Django 3.0.5 on 2020-08-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0114_auto_20200809_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('C', 'Low Value items'), ('A', 'high value items'), ('B', 'Medium value items')], default='B', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('F', 'fast moving items'), ('M', 'medium moving items'), ('S', 'slow moving items')], default='M', max_length=1),
        ),
    ]
