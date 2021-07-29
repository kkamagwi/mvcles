from django import forms
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text', 'img', "tag")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.URLInput(attrs={'class':'form-control'}),
    }