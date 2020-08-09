from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
import json
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from submissions.models import Submission
from rest_framework.exceptions import ValidationError

def register(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('start_application')
    return render(request, 'register.html', context)

def register_and_login(request):
    if request.method == 'POST' and request.is_ajax():
        # existing_user =
        json_data = json.loads(request.body)
        email = json_data.get('email')
        password = json_data.get('password')
        if not email or not password:
            return JsonResponse(
                {
                    "email": "This field is required",
                    "password": "This field is required"
                },
                status=400
            )
        try:
            user = User.objects.create_user(email, email, password)
        except IntegrityError:
            user = User.objects.get(username=email, email=email)

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
        return JsonResponse(
            {
                "message": "User created"
            },
            status=200
        )
    else:
        return JsonResponse(
            {
                "error": "there was a problem.",
                "email": "This field is required",
                "password": "This field is required"
            },
        status=400
        )

def start_application(request):
    context = {}
    return render(request, 'start-application.html', context)


def plaid_connect(request):
    user = request.user
    existing_submission = None
    if user:
        existing_submission = Submission.objects.filter(user=user).first()
    context = {'existing_submission': existing_submission}
    return render(request, 'plaid-connect.html', context)


def success(request):
    user = request.user
    existing_submission = None
    if user:
        existing_submission = Submission.objects.filter(user=user).first()
    context = {'existing_submission': existing_submission}
    return render(request, 'success.html', context)


# def login(request):
#     context = {}
#     return render(request, 'login.html', context)
