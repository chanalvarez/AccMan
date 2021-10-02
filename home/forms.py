from django import forms
from django.forms import ModelForm


from home.models import Account

class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'