from django import forms
from book.models import Book


class BookCreation(forms.ModelForm):


    class Meta:
        model = Book
        fields = ["name", "price", "creator", "author"]

    def clean_price(self):
        price = self.cleaned_data['price']
        if price > 10000 or price <= 10:
            raise forms.ValidationError("price must be between 11 to 10,000")
        return price

    # def clean_creator(self):
    #     creator = self.cleaned_data['creator']
    #     if creator is not :
    #         raise forms.ValidationError("creator not matched")
    #     return  creator