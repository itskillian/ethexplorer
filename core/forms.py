from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(
        label='', 
        max_length=42,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by address', 
                'autocomplete': 'off'
            }
        )
    )


class ConversionForm(forms.Form):
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('ETH', 'ETH'),
    ]
    
    amount = forms.DecimalField(
        label='Amount', 
        decimal_places=18,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter amount to convert', 
                'autocomplete': 'off'
            }
        )
    )
    
    from_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, initial='USD')
    to_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, initial='ETH')