import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import News, Categories

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'context', 'category', 'photo', 'is_bool']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search(r'\d', title):
            raise ValidationError('Title maydonida raqam bo‘lmasligi kerak')
        return title



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-cantrol'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-cantrol'}))


    class Meta:
        model = User
        fields = ('username','password')
