# Generated by Django 2.2 on 2019-04-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0013_remove_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(default=None, on_delete=models.SET(None), to='Tips.Location'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.OneToOneField(default=None, on_delete=models.SET(None), to='Users.Profile'),
        ),
    ]