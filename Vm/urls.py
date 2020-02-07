from .import view
from django.urls import path

urlpatterns = [
    path('', view.hello),
]
