from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime , timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = email.split('@')[0]
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True , null=True, verbose_name="سن")
    email = models.EmailField(unique=True , verbose_name="ایمیل")
    img = models.ImageField(upload_to='uploads/profiles/' , blank=True, verbose_name="تصویر کاربر")

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"username": self.username})
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
class OTP(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    code = models.CharField(max_length=6, verbose_name="رمز")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    expires_at = models.DateTimeField(verbose_name="زمان انقضاء")

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = datetime.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.email}"
    class Meta:
        verbose_name = "رمز یک بار مصرف"
        verbose_name_plural = "رمز های یکبار مصرف"


    

