# Generated by Django 2.2 on 2019-04-13 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0021_auto_20190413_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
    ]
