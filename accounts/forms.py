from  django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
        # super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None
            
    class Meta:
        model = CustomUser
        fields = ('username' ,'first_name','last_name' , 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username' , 'email' , 'age' ,)