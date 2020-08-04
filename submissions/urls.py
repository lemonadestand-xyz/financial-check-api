from django.urls import path

from .views import dashboard, single_submission

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('submission/<int:submission_id>/', single_submission, name="submission-detail"),
]