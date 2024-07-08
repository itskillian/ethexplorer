from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(
        label='', 
        max_length=42,
        widget=forms.TextInput(attrs=
                               {'placeholder': 'Search', 'autocomplete': 'off'},
                               ),
    )