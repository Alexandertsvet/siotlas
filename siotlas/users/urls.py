from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from users.views import MyPasswordResetView #, MyPasswordResetDoneView
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('accounts/logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('accounts/password_reset/', MyPasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            email_template_name = 'users/password_reset_email.html',
            ),name='password_reset'),
    path('account/password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
