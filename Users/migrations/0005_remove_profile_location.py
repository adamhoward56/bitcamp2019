# Generated by Django 2.2 on 2019-04-13 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20190413_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
