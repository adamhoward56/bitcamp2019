from django.db import models
from Users.models import Profile
from django.contrib import admin
from Tips.models import *

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " (" + self.lat + ", " + self.lon + ")"

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=240)

    def __str__(self):
        return "#" + self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=240)
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    is_question = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default=None, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, default=None, null=True)
    tags = models.ManyToManyField('Tips.Tag', blank=True)

    # Create a string describing the question
    def __str__(self):
        out = self.title
        q_type = "[TIP] "
        max_chars = 30

        if len(self.title) > max_chars:
            out = self.title[0:max_chars] + "..."
        if (self.is_question):
            q_type = "[QUESTION] "

        return q_type + "\"" + out + "\" @" + self.author.user.username

# Comment Object
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=240)
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.SET(None))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField('Tips.Tag', blank=True)

    def __str__(self):
        max_chars = 30
        if len(self.content) > max_chars:
            out = self.content[0:max_chars] + "..."

        return "[Post " + str(self.post.id) + ", Comment " + str(self.id) + "] \"" + self.content + "\""

# Register the models with the admin site
admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Tag)