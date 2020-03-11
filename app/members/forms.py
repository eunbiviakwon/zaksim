from django import forms


class LoginForm(forms.Form):
    pass


class SignupForm(forms.Form):
    def save(self):
        pass