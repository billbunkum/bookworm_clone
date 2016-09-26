from django.contrib.auth.forms import AuthenticationForm

from core.forms import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass