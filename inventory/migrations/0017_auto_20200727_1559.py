# Generated by Django 3.0.5 on 2020-07-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20200727_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('S', 'slow moving items'), ('F', 'fast moving items'), ('M', 'medium moving items')], default='M', max_length=1),
        ),
    ]
