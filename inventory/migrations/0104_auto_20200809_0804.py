# Generated by Django 3.0.5 on 2020-08-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0103_auto_20200809_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('S', 'slow moving items'), ('F', 'fast moving items'), ('M', 'medium moving items')], default='M', max_length=1),
        ),
    ]
