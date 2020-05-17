from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required=True)
    certificate = forms.FileField(required=True)
    expiring = forms.DateField(required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "certificate", "city", "expiring", "image", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']
        user.certificate = self.cleaned_data['certificate']
        user.expiring = self.cleaned_data['expiring']
        user.image = self.cleaned_data['image']
        if commit:
            user.save()
        return user
