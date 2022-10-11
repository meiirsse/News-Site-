from django import forms
from .models import News
import re

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    password = forms.CharField(label = 'password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



# we can add help_text='' in the future, for prompting users.
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'class': 'form-control'}))  
    password1 = forms.CharField(label = 'password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label = 'password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
     
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class NewsForm(forms.ModelForm):
     class Meta:
          model = News
          fields = ['title', 'content', 'is_published', 'category']
          widgets = {
               'title': forms.TextInput(attrs={'class': 'form-control'}),
               'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
               'category': forms.Select(attrs={'class': 'form-control'})
          }
     
     def clean_title(self):
          title = self.cleaned_data['title']
          if re.match(r'\d', title):
              raise ValidationError('The name must not begin with a number.')
          return title