from django import forms

class GetCountry(forms.Form):
    country_iso = forms.CharField(label="ISO 3 Code", max_length = 3)