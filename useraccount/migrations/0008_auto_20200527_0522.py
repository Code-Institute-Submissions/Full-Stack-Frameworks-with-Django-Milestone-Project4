# Generated by Django 2.2.6 on 2020-05-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0007_auto_20200527_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
