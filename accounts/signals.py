from django.dispatch import receiver
from django.db.models.signals import post_save
#from .models import Profile
from django.contrib.auth import get_user_model

UserModel = get_user_model()


#@receiver(post_save, sender=UserModel)
#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   #     instance.profile.save()

