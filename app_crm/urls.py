from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/token',views.CustomTokenObtainPairView.as_view(),name='CustomTokenObtainPairView'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sale_punch_submit', views.SalePunchSubmit.as_view(), name='sale_punch_submit'),
    # path('sale_punch_get', views.SalePunchGet.as_view(), name='sale_punch_get'),
]