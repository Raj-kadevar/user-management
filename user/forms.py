from django import forms
from user.models import UserEmployee


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserEmployee
        fields = ["username", "email", "password", "phone_number", "address"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if UserEmployee.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("password not matched")
        return confirm_password

    def clean_phone_number(self):
        number = self.cleaned_data["phone_number"]
        if len(str(number)) != 10:
            raise forms.ValidationError("Please enter 10 digit")
        elif not number.isdigit():
            raise forms.ValidationError("Please enter number only")
        else:
            if UserEmployee.objects.filter(phone_number=number).exists():
                raise forms.ValidationError("This number is already taken.")
        return number

class UpdateForm(forms.ModelForm):
    class Meta:
        model = UserEmployee
        fields = ["username", "email", "phone_number", "address"]
