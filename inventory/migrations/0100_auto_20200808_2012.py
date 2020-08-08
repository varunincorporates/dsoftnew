# Generated by Django 3.0.6 on 2020-08-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0099_auto_20200808_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('B', 'Medium value items'), ('A', 'high value items'), ('C', 'Low Value items')], default='B', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('M', 'medium moving items'), ('F', 'fast moving items'), ('S', 'slow moving items')], default='M', max_length=1),
        ),
    ]
