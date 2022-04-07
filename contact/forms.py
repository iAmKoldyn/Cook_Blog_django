from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta(type):
        model = ContactModel
        fields = "__all__"
