from django import forms
from .models import ProductLink

from django import forms
from .models import ProductLink

class ProductLinkForm(forms.ModelForm):
    class Meta:
        model = ProductLink
        fields = ['title', 'url', 'category']

class EmailForm(forms.Form):
    email = forms.EmailField()

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)
