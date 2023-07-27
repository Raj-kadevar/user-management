from django import forms
from user.models import User
class Reg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number', 'address']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if User.objects.filter(password=password).exists():
            raise forms.ValidationError("This password is already taken.")
        return password

    def clean_phone_number(self):
        number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=number).exists():
            raise forms.ValidationError("This number is already taken.")
        elif len(str(number)) != 10:
            raise forms.ValidationError("Please enter 10 digit")
        else:
            for i in number:
                if i not in ('1','2','3','4','5','6','7','8','9','0'):
                    raise forms.ValidationError("Please enter number only")
        return number