# Generated by Django 2.1 on 2019-07-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190704_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='in_time',
        ),
        migrations.RemoveField(
            model_name='viewer',
            name='out_time',
        ),
        migrations.AddField(
            model_name='viewer',
            name='no_of_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lat',
            field=models.FloatField(default=12.9333),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lng',
            field=models.FloatField(default=79.1333),
        ),
    ]
