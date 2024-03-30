from django import forms

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9)

    def clean(self):
        quantity = self.cleaned_data['quantity']
        if int(quantity) > 9:
            raise forms.ValidationError('The number of products in the order should not be more than 9')
        return quantity
