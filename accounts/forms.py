from django import forms
from django.contrib.auth.models import User
from .models import *



error = {
    'min_length' : 'حداقل می بایست 5 کاراکتر باشد',
    'required' : 'این فیلد اجباری است',

}
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'placeholder' : 'نام کاربری خود را وارد نمایید'}))
    email = forms.EmailField(error_messages=error,widget=forms.EmailInput(attrs={'placeholder' : 'ایمیلی خود را وارد نمایید'}))
    first_name = forms.CharField(max_length=50 , min_length=5 ,error_messages=error)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50 ,widget=forms.PasswordInput(attrs={'palaceholder' : 'رمز عبور خود را وارد نمایید'}))
    password_2 = forms.CharField(max_length=50 ,widget=forms.PasswordInput(attrs={'palaceholder' : 'رمز عبور خود را تکرار نمایید'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise forms.ValidationError('این نام کاربری از قبل موجود است')
        return user
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این پست الکترونیکی از قبل موجود است')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2 :
            raise forms.ValidationError('password not match')
        elif len(password2) < 8 :
            raise forms.ValidationError('password is short')
        elif not any (x.isupper() for x in password2) :
            raise forms.ValidationError('پسورد می بایست حداقل یک کاراکتر بزرگ داشته باشد')


        return password2

class UserLoginForm(forms.Form) :
    user = forms.CharField()
    password = forms.CharField()


class UserUpdateForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ['email' , 'first_name' , 'last_name']

class ProfileUpdateForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = ['phone' , 'address' ]