from django import forms
from django.contrib.auth.forms import UserChangeForm , AuthenticationForm , UserCreationForm , UsernameField
from django.forms.widgets import PasswordInput , TextInput
from .models import CustomUser

class EmailForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
    widget=forms.TextInput(attrs={"placeholder" :  "ایمیل" , "type" : "email"})        
    )

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6,
                                  label="رمز یک بار مصرف",
        widget=forms.TextInput(attrs={"placeholder" :  "کد عبور"})
        )



class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username' , 'img' , 'first_name' , 'last_name' , 'email' , 'age' ]
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'نام کاربری'}),
            'first_name' : forms.TextInput(attrs={'placeholder' : 'نام'}),
            'last_name' : forms.TextInput(attrs={'placeholder' : 'نام خانوادگی'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'ایمیل'}),
            'age' : forms.NumberInput(attrs={'placeholder' : 'سن'}),
            'img' : forms.FileInput(),
        }
        labels = {
            'username' : 'نام کاربری',
            'img' : 'تصویر پروفایل',
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی',
            'email' : 'ایمیل',
            'age' : 'سن'
        }
        help_texts = {
            'username' : ''
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        exclude = []


