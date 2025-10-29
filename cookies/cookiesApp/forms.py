from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(label='Item Name', max_length=100)
    quantity = forms.IntegerField(label='Quantity', min_value=1)