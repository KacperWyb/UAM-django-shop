# Generated by Django 2.2.12 on 2021-06-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210608_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zamówiony_przez',
            new_name='ordered_by',
        ),
    ]
