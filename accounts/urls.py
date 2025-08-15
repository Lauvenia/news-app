from django.urls import path, include
from .views import signup, select_publisher
from django.contrib.auth.views import LoginView

urlpatterns = [
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path("signup/", signup, name="signup"),
    path("select-publisher/", select_publisher, name="select_publisher"),
    path("", include("django.contrib.auth.urls")),
]
