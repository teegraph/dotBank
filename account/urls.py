from django.urls import path
import account.views as account


urlpatterns = [
    path('ping', account.ping),
    path('add', account.add),
    path('substract', account.substract),
    path('status', account.status),
]