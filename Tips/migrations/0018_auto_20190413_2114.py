# Generated by Django 2.2 on 2019-04-13 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0017_auto_20190413_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Profile'),
        ),
    ]
