from rest_framework import serializers
from .models import Profile, Invoice, Payment, Subscription, Notification
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'profile_id', 
            'username', 
            'email', 
            'password',
            'phone',
            'created_at',
            'updated_at'
            ]
        
class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'invoice_id',
            'profile_id',
            'amount',
            'status',
            'created_at',
            'updated_at',
            'due_date',
            'paid_date'
            ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'payment_id',
            'invoice_id',
            'amount',
            'status',
            'created_at',
            'updated_at',
            'paid_date',
            'payment_method',
            'payment_gateway'
            ]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'subscription_id',
            'profile_id',
            'plan_id',
            'status',
            'created_at',
            'updated_at',
            'start_date',
            'end_date',
            'next_billing_date',
            'payment_method',
            'payment_gateway',
            'amount'
            ]
        
class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'notification_id',
            'profile_id',
            'message',
            'created_at',
            'updated_at'
            ]
