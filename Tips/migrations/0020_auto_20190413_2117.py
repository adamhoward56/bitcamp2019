# Generated by Django 2.2 on 2019-04-13 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_profile'),
        ('Tips', '0019_auto_20190413_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tips.Location'),
        ),
    ]
