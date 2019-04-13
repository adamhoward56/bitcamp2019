# Generated by Django 2.2 on 2019-04-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0023_auto_20190413_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(to='Tips.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='Tips.Tag'),
        ),
    ]
