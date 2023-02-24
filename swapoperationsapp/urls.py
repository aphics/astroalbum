from django.urls import path

from . import views

urlpatterns = [
    path('swap_pool', views.swap_pool, name='swap_pool'),
] 