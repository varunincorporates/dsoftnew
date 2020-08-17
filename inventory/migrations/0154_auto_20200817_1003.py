# Generated by Django 3.0.6 on 2020-08-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0153_auto_20200817_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('C', 'Low Value items'), ('B', 'Medium value items'), ('A', 'high value items')], default='B', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('F', 'fast moving items'), ('M', 'medium moving items'), ('S', 'slow moving items')], default='M', max_length=1),
        ),
    ]
