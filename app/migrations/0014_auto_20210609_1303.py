# Generated by Django 2.2.12 on 2021-06-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210609_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
