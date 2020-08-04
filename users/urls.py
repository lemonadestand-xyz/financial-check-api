from django.urls import path

from .views import register, start_application, plaid_connect, register_and_login

urlpatterns = [
    path('register/', register, name="register"),
    path('register-ajax/', register_and_login, name="register_and_login"),
    path('start-application/', start_application, name="start_application"),
    path('plaid-connect/', plaid_connect, name="plaid_connect"),
]
