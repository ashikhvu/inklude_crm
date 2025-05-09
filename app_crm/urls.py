from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sale_punch_submit', views.SalePunchSubmit.as_view(), name='sale_punch_submit'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document=settings.MEDIA_ROOT)