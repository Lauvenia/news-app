from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "email",
            "role",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "email",
            "role",
            "publisher",
            "subscribed_journalists",
            "subscribed_publishers",
        )


class SelectPublisher(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["publisher"]