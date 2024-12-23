from django import forms
from django.contrib.auth.models import User
from AdminApp.models import Blog,UserProfile
from django.contrib.auth import get_user_model




class LoginForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["username","password","usertype"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
            'usertype': forms.Select(attrs={'class': 'form-select', 'placeholder': 'User Type'}),
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"})
        }

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Description"}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input'}),
         }