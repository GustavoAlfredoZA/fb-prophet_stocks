from django import forms

class FundamentalForm(forms.Form):
    Ticker = forms.CharField(label='Ticker', max_length=100)
