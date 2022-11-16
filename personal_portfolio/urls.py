from django.urls import path

from personal_portfolio.views import index

urlpatterns = [
    path('', index)
]
