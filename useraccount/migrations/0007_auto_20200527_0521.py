# Generated by Django 2.2.6 on 2020-05-27 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0006_remove_orders_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
