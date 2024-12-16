from django.urls import path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

app_name = 'api'

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/swagger/')),
]

router = DefaultRouter()
