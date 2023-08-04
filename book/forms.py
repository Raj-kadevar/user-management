from django import forms
from book.models import Book


class BookCreation(forms.ModelForm):


    class Meta:
        model = Book
        fields = ["name", "price", "creator", "author"]

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError("Name is required")
        return name
    def clean_price(self):
        price = self.cleaned_data['price']
        if price > 10000 or price <= 10:
            raise forms.ValidationError("price must be between 11 to 10,000")
        return price
