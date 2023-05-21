# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views


from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'), ),
    path('password_reset_done/', auth_views.PasswordChangeView.as_view(template_name='password_reset_done.html'), ),
]