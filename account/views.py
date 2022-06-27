import logging
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, RedirectView, View
from account.forms import SignUpForm, LoginForm


logger = logging.getLogger(__name__)


User = get_user_model()


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("account:check_email")

    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = form.save()
        user.is_active = False  # Turns the user status to inactive
        user.save()

        form.send_activation_email(self.request, user)

        return to_return


class AccountVerificationView(RedirectView):
    url = reverse_lazy("blog:home")

    def get(self, request):
        try:
            user_id = request.GET.get("user_id")
            email = request.GET.get("email")

            user = User.objects.get(id=user_id, email=email)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.save()
                auth_login(request, user)
                return super().get(request)
            else:
                return redirect("blog:home")
        else:
            return render(request, "account/account_invalid.html")


class LoginView(View):
    template_name = "account/login.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect("blog:home")

        message = "Invalid email/password!"
        msg_type = "error"

        return render(
            request,
            self.template_name,
            context={"form": form, "message": message, "msg_type": msg_type},
        )


class CheckEmailView(TemplateView):
    template_name = "account/check_email.html"


class SuccessView(TemplateView):
    template_name = "account/account_activation_success.html"
