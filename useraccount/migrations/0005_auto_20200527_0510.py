# Generated by Django 2.2.6 on 2020-05-27 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_orders_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total_cost',
            field=models.CharField(max_length=100),
        ),
    ]