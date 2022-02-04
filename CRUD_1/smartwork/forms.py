from tkinter import Widget
from django import forms
from.models import user

class studentregister(forms.ModelForm):
    class Meta:
        model=user
        fields=['id','name','email','password','mobile_no']
        Widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'mobile_no':forms.TextInput(attrs={'class':'form-control'})}
  
  