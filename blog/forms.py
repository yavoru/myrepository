from django import forms
from .models import *
from django.contrib.auth.models import User
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['body','image','category']
        widgets={
            'body':forms.Textarea(attrs={'class':'form_control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),  
            'category': forms.Select(attrs={'class': 'form-control'})  # Correct widget for ModelChoiceField
        }

class SignUpForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Account
        fields=['name','email','password']
    def clean_username(self):
        password=self.cleaned_data.get('password')
        uname=self.cleaned_data.get('user')
        if User.objects.filter(user=uname).first():
            raise forms.ValidationError(
                "Customer with this username already exists."
            )
        return uname

class LogInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            #Issue is here, because this field is required
            #But I want it to be linked to request.user.id
            "author",
            #The remaining fields will be shown through the form
            "body",
            "image",
            "category",
            ]