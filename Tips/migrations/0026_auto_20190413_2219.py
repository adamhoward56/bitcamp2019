# Generated by Django 2.2 on 2019-04-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0025_auto_20190413_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(None), to='Users.Profile'),
        ),
    ]
