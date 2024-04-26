from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, generics, viewsets
from .models import Profile, Invoice, Payment, Subscription, Notification
from .serializers import UserSerializer, InvoicesSerializer, PaymentSerializer, SubscriptionSerializer, NotificationsSerializer

# Create your views here.

# Use generic views instead of viewsets
class UserList(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class InvoicesList(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoicesSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentList(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionList(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationsList(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]





