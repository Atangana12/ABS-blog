from django import forms
from django.forms import fields
from . models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'name',
            'email',
            'body'
        }

#class ContactForm(forms.ModelForm):
    #class Meta:
       # model = Contact
        #fields = '__all__'   

#class UserForm(forms.ModelForm):
    #class Meta:
       # model = User
        fields = '__all__'