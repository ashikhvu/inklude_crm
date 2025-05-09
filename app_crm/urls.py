from django.urls import path
from . import views

urlpatterns = [
    path('sale_punch_submit', views.SalePunchSubmit.as_view(), name='sale_punch_submit'),
]