from rest_framework import urlpatterns
from django.urls import path, include
from .views import UserList, InvoicesList, PaymentList, SubscriptionList, NotificationsList
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'user-profile', UserList, basename='user-profile')
# router.register(r'user-profile/<str:pk>', UserList, basename='user-profile-pk')
# router.register(r'user-profile/<str:pk>/invoices', InvoicesList, basename='user-profile-invoices')
# router.register(r'user-profile/<str:pk>/invoices/<str:pk>', InvoicesList, basename='user-profile-invoices-pk')
# router.register(r'user-profile/<str:pk>/invoices/<str:pk>/payments', PaymentList, basename='user-profile-invoices-payments')
# router.register(r'user-profile/<str:pk>/invoices/<str:pk>/payments/<str:pk>', PaymentList, basename='user-profile-invoices-payments-pk')
# router.register(r'user-profile/<str:pk>/subscriptions', SubscriptionList, basename='user-profile-subscriptions')
# router.register(r'user-profile/<str:pk>/subscriptions/<str:pk>', SubscriptionList, basename='user-profile-subscriptions-pk')
# router.register(r'user-profile/<str:pk>/notifications', NotificationsList, basename='user-profile-notifications')
# router.register(r'user-profile/<str:pk>/notifications/<str:pk>', NotificationsList, basename='user-profile-notifications-pk')
# router.register(r'invoices', InvoicesList, basename='invoices')
# router.register(r'invoices/<str:pk>', InvoicesList, basename='invoices-pk')
# router.register(r'payments', InvoicesList, basename='payments')
# router.register(r'payments/<str:pk>', PaymentList, basename='payments-pk')
# router.register(r'subscriptions', SubscriptionList, basename='subscriptions')
# router.register(r'subscriptions/<str:pk>', SubscriptionList, basename='subscriptions-pk')
# router.register(r'notifications', NotificationsList, basename='notifications')
# router.register(r'notifications/<str:pk>', NotificationsList, basename='notifications-pk')

# urlpatterns += router.urls

# urlpatterns = [
#     path('user-profile/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile'),
#     path('user-profile/<str:pk>', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-profile-primary-key'),
#     path('user-profile/<str:pk>/invoices', InvoicesViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile-invoices'),
#     path('user-profile/<str:pk>/invoices/<str:pk>', InvoicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-profile-invoices-primary-key'),
#     path('user-profile/<str:pk>/invoices/<str:pk>/payments', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile-invoices-payments'),
#     path('user-profile/<str:pk>/invoices/<str:pk>/payments/<str:pk>', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='user-profile-invoices-payments-primary-key'),
#     path('user-profile/<str:pk>/subscriptions', SubscriptionViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile-subscriptions'),
#     path('user-profile/<str:pk>/subscriptions/<str:pk>', SubscriptionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-profile-subscriptions-primary-key'),
#     path('user-profile/<str:pk>/notifications', NotificationsViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile-notifications'),
#     path('user-profile/<str:pk>/notifications/<str:pk>', NotificationsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-profile-notifications-primary-key'),
#     path('invoices/', InvoicesViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoices'),
#     path('invoices/<str:pk>', InvoicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='invoices-primary-key'),
#     path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payments'),
#     path('payments/<str:pk>', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='payments-primary-key'),
#     path('subscriptions/', SubscriptionViewSet.as_view({'get': 'list', 'post': 'create'}), name='subscriptions'),
#     path('subscriptions/<str:pk>', SubscriptionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='subscriptions-primary-key'),
#     path('notifications/', NotificationsViewSet.as_view({'get': 'list', 'post': 'create'}), name='notifications'),
#     path('notifications/<str:pk>', NotificationsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notifications-primary-key'),
# ]
