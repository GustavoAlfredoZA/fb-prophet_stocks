from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'Fundamental', views.FundamentalView.as_view(), name='Fundamental'),
]
