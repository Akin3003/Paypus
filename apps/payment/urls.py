from django.urls import path

from apps.payment.views import InitiatePaymentView, PaystackWebhookView, PaystackCallbackView

urlpatterns = [
    path('orders/<int:order_id>/initiate/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('webhook/paystack/', PaystackWebhookView.as_view(), name='paystack-webkook'),
    path('callback/', PaystackCallbackView.as_view(), name='paystack-callback'), #Placeholder for now
]