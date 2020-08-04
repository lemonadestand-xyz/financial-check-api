from django.contrib import admin

from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


admin.site.register(Submission, SubmissionAdmin)
