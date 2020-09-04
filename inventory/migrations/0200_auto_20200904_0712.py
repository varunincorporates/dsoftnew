# Generated by Django 3.0.6 on 2020-09-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0199_auto_20200824_1740'),
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
            field=models.CharField(choices=[('S', 'slow moving items'), ('M', 'medium moving items'), ('F', 'fast moving items')], default='M', max_length=1),
        ),
    ]
