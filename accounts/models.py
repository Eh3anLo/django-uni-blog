from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True , null=True)
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='media/uploads/images/2024/06' , blank=True)

    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"username": self.username})
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    

