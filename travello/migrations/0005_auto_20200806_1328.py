# Generated by Django 3.0.6 on 2020-08-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200806_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='product',
        ),
        migrations.AlterField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='category',
            field=models.CharField(choices=[('B', 'Medium value items'), ('C', 'Low Value items'), ('A', 'high value items')], max_length=200, null=True),
        ),
    ]
