from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_request, name='submit_request'),
    path('status/', views.request_status, name='request_status'),
]