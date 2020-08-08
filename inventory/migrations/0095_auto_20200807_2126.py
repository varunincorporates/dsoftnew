# Generated by Django 3.0.5 on 2020-08-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0094_auto_20200806_1344'),
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
            field=models.CharField(choices=[('S', 'slow moving items'), ('F', 'fast moving items'), ('M', 'medium moving items')], default='M', max_length=1),
        ),
    ]
