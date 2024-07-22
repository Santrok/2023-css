from django import forms

PRODUCT_QUANTITY = [(i, str(i)) for i in range(1,11)]

s = []

for i in range(1,21):
    s.append((i, str(i)))

class AddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)