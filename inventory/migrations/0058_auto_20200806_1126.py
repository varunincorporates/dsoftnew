# Generated by Django 3.0.6 on 2020-08-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0057_auto_20200806_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('C', 'Low Value items'), ('A', 'high value items'), ('B', 'Medium value items')], default='B', max_length=10),
        ),
    ]