# orders/forms.py
from django import forms

class OrderForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Имена")
    email = forms.EmailField(label="Имейл")
    phone = forms.CharField(max_length=20, label="Телефон")
    address = forms.CharField(widget=forms.Textarea, label="Адрес за доставка")
    consent_to_privacy_policy = forms.BooleanField(label="Съгласен съм с политиката за поверителност", required=True)

