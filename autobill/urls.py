"""
URL configuration for autobill project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from billing.views import UserList, InvoicesList, PaymentList, SubscriptionList, NotificationsList

router = routers.DefaultRouter()
router.register(r'user-profile', UserList, basename='user-profile')
router.register(r'user-profile/<str:pk>', UserList, basename='user-profile-pk')
router.register(r'user-profile/<str:pk>/invoices', InvoicesList, basename='user-profile-invoices')
router.register(r'user-profile/<str:pk>/invoices/<str:pk>', InvoicesList, basename='user-profile-invoices-pk')
router.register(r'user-profile/<str:pk>/invoices/<str:pk>/payments', PaymentList, basename='user-profile-invoices-payments')
router.register(r'user-profile/<str:pk>/invoices/<str:pk>/payments/<str:pk>', PaymentList, basename='user-profile-invoices-payments-pk')
router.register(r'user-profile/<str:pk>/subscriptions', SubscriptionList, basename='user-profile-subscriptions')
router.register(r'user-profile/<str:pk>/subscriptions/<str:pk>', SubscriptionList, basename='user-profile-subscriptions-pk')
router.register(r'user-profile/<str:pk>/notifications', NotificationsList, basename='user-profile-notifications')
router.register(r'user-profile/<str:pk>/notifications/<str:pk>', NotificationsList, basename='user-profile-notifications-pk')
router.register(r'invoices', InvoicesList, basename='invoices')
router.register(r'invoices/<str:pk>', InvoicesList, basename='invoices-pk')
router.register(r'payments', InvoicesList, basename='payments')
router.register(r'payments/<str:pk>', PaymentList, basename='payments-pk')
router.register(r'subscriptions', SubscriptionList, basename='subscriptions')
router.register(r'subscriptions/<str:pk>', SubscriptionList, basename='subscriptions-pk')
router.register(r'notifications', NotificationsList, basename='notifications')
router.register(r'notifications/<str:pk>', NotificationsList, basename='notifications-pk')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('billing/', include(router.urls)),
]

