
import re
from django import forms
from django.core.exceptions import ValidationError
from .models import News, Categories
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'context', 'category', 'photo', 'is_bool']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search(r'\d', title):
            raise ValidationError('Title maydonida raqam bo‘lmasligi kerak')
        return title
