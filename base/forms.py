# from django.forms import ModelForm
# from .models import Room
# from django import forms
# from django.contrib.auth.models import User

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User




# class RoomForm(ModelForm):
#     class Meta:
#         model=Room
#         fields='__all__'
#         exclude=['host','participants']
    
    


 # class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")    
        
         
        


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']        