from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Book(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,)
    id = models.AutoField(primary_key=True)
    user_image = models.ImageField(
        upload_to="static/images", default='abc.png')
    user_name = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to="static/images")
    book_name = models.CharField(max_length=50)
    book_category = models.CharField(max_length=50)
    book_outher = models.CharField(max_length=50)
    user_mobile_no = models.IntegerField()
    book_info = models.CharField(max_length=500)
    user_address = models.CharField(max_length=500)

    def __str__(self):
        return self.book_name


# contact us
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


# user profile pic ################

class Profile(models.Model):
    # Delete profile when user is deleted
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='static/profile_pic', null=True, default='abc.png')

    def __str__(self):
        # show how we want it to be displayed
        return f'{self.profile_user.username} Profile'

# create by sagar kakade


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_user=instance)
    instance.profile.save()


# Users Following System

class FollowersCount(models.Model):
    follower = models.IntegerField()
    user = models.IntegerField()

    def __str__(self):
        useris = ""
        for i in User.objects.filter(id=self.user):
            useris = i.username

        followeris = ""
        for i in User.objects.filter(id=self.follower):
            followeris = i.username

        return f"{followeris} folllow {useris}"
