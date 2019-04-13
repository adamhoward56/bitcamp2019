# Generated by Django 2.2 on 2019-04-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_profile'),
        ('Tips', '0005_auto_20190413_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=240)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=models.SET(None), to='Users.Profile')),
            ],
        ),
    ]
