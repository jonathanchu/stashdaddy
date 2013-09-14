from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', max_length=30,
                                error_messages={'invalid': 'This value must contain only letters, numbers, and underscores.'})
    email = forms.EmailField(max_length=75)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    # def clean_username(self):
    #     existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
    #     if existing.exists():
    #         raise forms.ValidationError(_("A user with that username already exists."))
    #     else:
    #         return self.cleaned_data['username']

    #     # try:
    #     #     user = User.objects.get(username__iexact=self.cleaned_data['username'])
    #     # except User.DoesNotExist:
    #     #     return self.cleaned_data['username']
    #     # raise forms.ValidationError("Username '%(username)s' is not available." % self.cleaned_data)

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data
