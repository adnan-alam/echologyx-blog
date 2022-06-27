from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


User = get_user_model()


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def send_activation_email(self, request, user):
        current_site = get_current_site(request)
        subject = "Activate Your Account"
        message = render_to_string(
            "email/account_verification_mail.html",
            {
                "domain": current_site.domain,
                "user_id": user.id,
                "email": user.email,
            },
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.send()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text="Enter a valid email address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("email", "password", "is_active", "is_admin")
