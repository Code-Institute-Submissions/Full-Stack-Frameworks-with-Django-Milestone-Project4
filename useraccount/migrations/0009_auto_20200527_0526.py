# Generated by Django 2.2.6 on 2020-05-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0008_auto_20200527_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.CharField(max_length=100),
        ),
    ]