# Generated by Django 3.0.6 on 2020-08-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0045_auto_20200805_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abc',
            field=models.CharField(choices=[('A', 'high value items'), ('B', 'Medium value items'), ('C', 'Low Value items')], default='B', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='fms',
            field=models.CharField(choices=[('M', 'medium moving items'), ('F', 'fast moving items'), ('S', 'slow moving items')], default='M', max_length=1),
        ),
    ]
