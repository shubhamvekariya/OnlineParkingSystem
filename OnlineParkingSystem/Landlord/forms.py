from django.forms import ModelForm , Textarea
from django import forms
from User.models import User_detail
from .models import Land_detail


class RegistrationForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('name','password','mobile_no','email','age','role')
        widgets = {
            'age': forms.NumberInput(attrs={
                "class":"input100",
                "id":"age",
                "placeholder":"Age"
            }),
            'name': forms.TextInput(attrs={
                "class":"input100",
                "id":"name",
                "placeholder":"Name"
            }),
            'mobile_no': forms.NumberInput(attrs={
                "class":"input100",
                "id":"mobile_no",
                "placeholder":"Mobile Number"
            }),
            'password': forms.PasswordInput(attrs={
                "class":"input100",
                "id":"password",
                "placeholder":"*********"
            }),
            'email': forms.EmailInput(attrs={
                "class":"input100",
                "id":"email",
                "placeholder":"Email Address..."
            }),
            'role': forms.HiddenInput(attrs={
                "id":"role",
                "value":"Landlord"
            }),
            
        }
        

class LoginForm(ModelForm):
    class Meta:
        model=User_detail
        fields=('email','password')
        widgets = {
            'password': forms.PasswordInput(attrs={
                "class":"input100",
                "id":"password",
                "placeholder":"Password"
            }),
            'email': forms.EmailInput(attrs={
                "class":"input100",
                "id":"email",
                "placeholder":"Email Address"
            })
        }



class AddLandForm(ModelForm):
    class Meta:
        model=Land_detail
        fields=('lattitude','langitude','address','images','no_of_spot','description','availability','price_per_hour','start_date','end_date','verified','userid')
        widgets = {
            'address': forms.TextInput(attrs={
                "class":"form-control",
                "id":"address",
                "placeholder":"Enter Your Address"
            }),
            'images': forms.FileInput(attrs={
                "class":"form-control",
                "id":"address",
                "placeholder":"Enter Your Address"
            }),
            'no_of_spot': forms.NumberInput(attrs={
                "class":"form-control",
                "id":"no_of_spot",
                "placeholder":"Enter Number of Spot"
            }),
            'description': forms.TextInput(attrs={
                "class":"form-control",
                "id":"description",
                "placeholder":"Enter Description"
            }),
            'price_per_hour': forms.NumberInput(attrs={
                "class":"form-control",
                "id":"price_per_hour",
                "placeholder":"Enter Price per Hour"
            }),
            'start_date': forms.DateInput(attrs={
                "class":"form-control",
                "id":"start_date",
            }),
            'end_date': forms.DateInput(attrs={
                "class":"form-control",
                "id":"end_date",
            }),
            
        }