from django import forms

class ContactForm(forms.Form):
    file = forms.FileField(required=False)
