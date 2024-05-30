from django.db import models
from accounts.models import CustomUser
# Create your models here.
class UserProfile(models.Model):
    UNI_MAJOR_LEVEL = {
        'CS1' : "Associate degree",
        'CS2' : "Bachelor's degree",
        'N1' : "Associate degree",
    }
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    bio = models.TextField(blank=True , null=True)
    major = models.CharField(max_length=200 , choices=UNI_MAJOR_LEVEL)
    profession = models.CharField(max_length=200)
    # pic = models.ImageField()

    def __str__(self):
        return self.user.username