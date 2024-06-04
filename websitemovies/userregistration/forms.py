from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profession', 'location', 'birth_date', 'mobile', 'profile_picture']