from django import forms
from .models import UserProfile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio' , 'major' , 'profession' , 'github_url' ,'linkedin_url']
        exclude = []

        widgets = {
            'bio' : forms.Textarea(attrs={'placeholder' : "معرفی ..."}),
            'major' : forms.Select(attrs={'placeholder' : "مدرک تحصیلی"}),
            'profession' : forms.TextInput(attrs={'placeholder' : "سمت شغلی"}),
        }
