from django.contrib.auth.forms import UserCreationForm
from .models import User 
from django import forms 

class CustomerForm(UserCreationForm):  
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter User Name"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Passsword"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your Confirm password"}))

    class Meta:  
        model = User
        fields = ["username", "email", "password1", "password2"]  


class ContactForms(forms.Form):
    name = forms.CharField(label="name",max_length=100,required=True)
    email = forms.EmailField(label="email" , required=True)
    message = forms.CharField(label="message" , required=True)
