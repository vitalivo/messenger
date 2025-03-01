from django import forms
from .models import Message, UserProfile


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']