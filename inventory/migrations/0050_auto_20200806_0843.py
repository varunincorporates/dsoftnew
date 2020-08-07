# Generated by Django 3.0.6 on 2020-08-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0049_auto_20200806_0439'),
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
            field=models.CharField(choices=[('M', 'medium moving items'), ('S', 'slow moving items'), ('F', 'fast moving items')], default='M', max_length=1),
        ),
    ]
