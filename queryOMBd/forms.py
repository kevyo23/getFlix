from django import forms

class SubmitQueryForm(forms.Form):
    url = forms.CharField(label='Submit query')
