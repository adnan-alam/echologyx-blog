from django.urls import path
from .views import (
    LoginView,
    SignUpView,
    AccountVerificationView,
    CheckEmailView,
    SuccessView,
)


app_name = "account"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "verify-account",
        AccountVerificationView.as_view(),
        name="verify_account",
    ),
    path("check-email/", CheckEmailView.as_view(), name="check_email"),
    path("success/", SuccessView.as_view(), name="success"),
]
