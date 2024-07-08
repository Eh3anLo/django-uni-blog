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

    
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':('نام کاربری')})
        self.fields['email'].widget.attrs.update({'placeholder':('ایمیل')})
        self.fields['password1'].widget.attrs.update({'placeholder':('رمز عبور')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('تکرار رمز عبور')})
        self.fields['first_name'].widget.attrs.update({'placeholder':('نام')})
        self.fields['last_name'].widget.attrs.update({'placeholder':('نام خانوادگی')})
    error_messages = {
        'password_mismatch': "رمز های عبور با هم مغایرت دارد",
    }
            
    class Meta:
        model = CustomUser
        fields = ('username' ,'first_name','last_name' , 'email',)
        error_messages = {
            'username': {
                'unique': 'این اسم قبلا بوده',
                'smilar' : "this is very bad"
            },
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username' , 'email' , 'age' , 'img')


class CustomAuthenticationForm(AuthenticationForm):
    TEXT_HOLDER = {
        "username" : "نام کاربری",
        "password" : "رمز عبور",
        "invalid_login" : "نام کاربری یا رمز عبور اشتباه است",
        "inactive" : "اکانت مورد نظر غیر فعال است",
        "required" : "این ورودی الزامی است"
    }
    username = UsernameField(
        label=("نام کاربری"),
        widget=TextInput(
        attrs={"autofocus": True, "placeholder" : TEXT_HOLDER['username']}),
        )
    error_messages = {
        "invalid_login": (
         TEXT_HOLDER["invalid_login"]
        ),
        "inactive": (TEXT_HOLDER["inactive"])
    }