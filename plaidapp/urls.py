from django.urls import path

from .views import ObtainAccessTokenView, AccountsListView, TransactionListView, asset_report

urlpatterns = [
    path('create-item/', ObtainAccessTokenView.as_view(), name="create_item"),
    path('accounts/', AccountsListView.as_view(), name="list_accounts"),
    path('transactions/', TransactionListView.as_view(), name="list_transactions"),
    path('asset-report/', asset_report, name="asset_report"),
]
