from django import forms


class PostCreateForm(forms.Form):
    image = forms.ImageField()
    text = forms.CharField()

