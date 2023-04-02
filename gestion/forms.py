from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class GiftForm(forms.Form):
    elección = forms.ChoiceField(label='Elección', widget=forms.RadioSelect())