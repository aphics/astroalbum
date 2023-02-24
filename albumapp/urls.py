from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'), 
    path('new_card', views.adquire_new_card, name='new_card'),
    path('card_info/<int:id>', views.card_info, name='card_info'),
    path('swap_card/<int:id>', views.swap_card, name='swap_card'),
    path('delete_card/<int:id>', views.delete_card, name='delete_card'),
    path('swap_status_card/<int:id>', views.swap_status_card, name='swap_status_card'),
] 