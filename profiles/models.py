from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    UNI_MAJOR_LEVEL = {
        'CS1' : "Computer Associate degree",
        'CS2' : "Computer Bachelor's degree",
        'N1' : "Network Associate degree",
    }
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    bio = models.TextField(blank=True , null=True)
    major = models.CharField(max_length=200 , choices=UNI_MAJOR_LEVEL , blank=True)
    profession = models.CharField(max_length=200 , blank=True)
    # pic = models.ImageField()

    def __str__(self):
        return self.user.username
    
# Create profile when new user signup
def create_profile(sender , instance , created , **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile , sender=CustomUser)


