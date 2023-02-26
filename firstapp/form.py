from django import forms


class NameForm(forms.Form):
    Annual_Income = forms.CharField()
    Annual_Income.widget = forms.TextInput(attrs={'class':"form-control"})
    Years_in_current_job = forms.CharField()
