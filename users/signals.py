from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# Create a profile whenever a new user registed
@receiver(post_save, sender=User) # when a user is saved, send a signal with an user instance to the create profile function
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
      
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     pass