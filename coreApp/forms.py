from django import forms
from .models import *

class FormPosts(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','content','tag']
