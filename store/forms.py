from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(label="",
    widget=forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"نام و نام خانوادگی خود را وارد نمایید"}))
    email = forms.EmailField(label="",
     widget=forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"ایمیل خود را وارد"}))
    message = forms.CharField(label="",
     widget=forms.Textarea(attrs={"class":"form-control mb-2", "placeholder":"متن پیام"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("ایمیل شما جیمیل نیست")
        return email

class LoginForm(forms.Form):
    userName = forms.CharField(label="",
        widget=forms.TextInput(attrs = {"class":"form-control", "placeholder":"نام کاربری"})
    )
    password = forms.CharField(label="",
         widget=forms.PasswordInput(attrs = {"class":"form-control", "placeholder":"کلمه عبور"})
    )


class RegisterForm(forms.Form):
    userName = forms.CharField(label="نام کاربری",
        widget=forms.TextInput(attrs = {"class":"form-control mb-2", "placeholder":"نام کاربری"})
    )
    email = forms.CharField(label="ایمیل",
         widget=forms.EmailInput(attrs = {"class":"form-control mb-2", "placeholder":"ایمیل"})
    )
    password = forms.CharField(label="کلمه عبور",
         widget=forms.PasswordInput(attrs = {"class":"form-control mb-2", "placeholder":"کلمه عبور"})
    )
    repassword = forms.CharField(label="تکرار کلمه عبور",
         widget=forms.PasswordInput(attrs = {"class":"form-control mb-5", "placeholder":"تایید کلمه عبور"})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get("userName")
        qs = User.objects.filter(username=userName)
        if qs.exists():
            raise forms.ValidationError("این نام کاربری موجود است")
        return userName

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("این ایمیل موجود است")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")

        if password != repassword:
            raise forms.ValidationError("تکرار پسورد صحیح نیست")

        return data