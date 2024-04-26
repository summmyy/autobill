from django.contrib import admin
from .models import Profile, Invoice, Payment, Subscription, Notification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(Notification)