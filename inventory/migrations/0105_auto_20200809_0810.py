# Generated by Django 3.0.5 on 2020-08-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0104_auto_20200809_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('C', 'Low Value items'), ('B', 'Medium value items'), ('A', 'high value items')], default='B', max_length=10),
        ),
    ]