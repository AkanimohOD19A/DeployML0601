from django import forms


class CustomerForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField()
    salary = forms.IntegerField()
