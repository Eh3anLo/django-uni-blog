from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    UNI_MAJOR_LEVEL = {
        'کاردانی' : "کاردانی نرم افزار",
        'کارشناسی' : "کارشناسی نرم افزار",
        'شبکه' : "شبکه و سخت و افزار",
    }
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="درباره من",blank=True , null=True)
    major = models.CharField(verbose_name="رشته تحصیلی",max_length=200 , choices=UNI_MAJOR_LEVEL , blank=True)
    profession = models.CharField(verbose_name="سمت شغلی",max_length=200 , blank=True)
    github_url = models.URLField((" گیت هاب"), max_length=500 , null=True , blank=True)
    linkedin_url = models.URLField((" لینکدین"), max_length=500 , null=True , blank=True)
    # pic = models.ImageField()

    def __str__(self):
        return self.user.username
    
# Create profile when new user signup
def create_profile(sender , instance , created , **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile , sender=CustomUser)


