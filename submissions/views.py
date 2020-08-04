from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from plaid.errors import PlaidError, InvalidInputError, InvalidRequestError
from plaid import Client


from .models import Submission
from .serializers import SubmissionSerializer

client = Client(
        client_id=settings.PLAID_CLIENT_ID,
        secret=settings.PLAID_SECRET,
        public_key=settings.PLAID_PUBLIC_KEY,
        environment=settings.PLAID_ENV
    )

def dashboard(request):
    context = {
        'show_search_bar': True,
        'awaiting_review_count': Submission.objects.filter(status='pending').count(),
        'submissions': Submission.objects.order_by('-created')[:20]
    }
    return render(request, 'dashboard.html', context)


def single_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    report = None

    try:
        liabilities = client.Liabilities.get(submission.item.access_token)
    except:
        liabilities = {}
    try:
        income = client.Income.get(submission.item.access_token)
    except:
        income = {}

    context = {
        'report': report,
        'liabilities': liabilities,
        'income': income.get('income'),
        'account_count': len(liabilities.get('accounts', [])) if liabilities else [],
        'submission': submission
    }
    return render(request, 'submissions/detail.html', context)


class SubmissionViewSet(ModelViewSet):
    """
   A viewset for viewing brands
   """

    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('created_on', 'name')
    search_fields = ('first_name', 'last_name')
    swagger_schema = None

    def get_queryset(self):
        return Submission.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super(SubmissionViewSet, self).create(request, *args, **kwargs)
