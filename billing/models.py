from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user_id } - {self.amount} - {self.status}'

class Payment(models.Model):
    payment_id = models.AutoField( primary_key=True)
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    payment_gateway = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.payment_id} - {self.invoice_id} - {self.amount} - {self.status}'

class Subscription(models.Model):
    subscription_id = models.AutoField( primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    next_billing_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    payment_gateway = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.subscription_id

class Notification(models.Model):
    notification_id = models.AutoField( primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notification_id



