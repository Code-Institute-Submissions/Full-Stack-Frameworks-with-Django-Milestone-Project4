# Generated by Django 2.2.6 on 2020-05-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_trip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='desc',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
