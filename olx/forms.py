from django import forms
from olx.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from.models import UserProfile
from olx.models import Products
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))



    class Meta:
        model=User
        fields=["email","username","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),

           
        
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))



class UserCreationForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['phone','address','profile' ]

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
