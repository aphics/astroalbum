from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
import random


@login_required(login_url='landing')
def home(request):
    user = request.user
    user_distinct_cards = Album.objects.filter(user_id=user).values(
        'catalogue_id', 'catalogue_id__messier', 'catalogue_id__name',
        'catalogue_id__image').distinct().order_by('catalogue_id')
    return render(request, 'home.html', {'cards': user_distinct_cards})


@login_required(login_url='landing')
def adquire_new_card(request):   

    def get_card_info(new_card):
        card_info = Album.objects.filter(pk=new_card.id).values(
            'catalogue_id__messier', 'catalogue_id__name', 'catalogue_id__type',
            'catalogue_id__ar', 'catalogue_id__dec', 'catalogue_id__dist', 
            'catalogue_id__description', 'catalogue_id__image' )
        return card_info

    if request.method == 'POST':
        user = request.user
        random_messier = Catalogue.objects.get(pk=random.randrange(1,Catalogue.objects.count()))
        new_card = Album(user_id=user.id, catalogue_id=random_messier.id, swap_status=False)
        new_card.save()
        new_card_info = get_card_info(new_card)
        return render(request, 'new_card.html', { 'card': new_card_info[0] })
    return render(request, 'new_card.html')

@login_required(login_url='landing')
def card_info(request, id):
    card_info = Catalogue.objects.get(id=id)   
    return render(request, 'card_info.html', { 'card': card_info })


@login_required(login_url='landing')
def swap_card(request, id):
    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=id)
    card_info =  Catalogue.objects.get(id=id)
    return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})

@login_required(login_url='landing')
def delete_card(request, id):
    card = Album.objects.get(id=id)
    card.delete()
    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=card.catalogue_id)
    if user_cards:
        card_info =  Catalogue.objects.get(id=card.catalogue_id)
        return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})
    else:
        return redirect('home')

@login_required(login_url='landing')
def swap_status_card(request, id):
    card = Album.objects.get(id=id)
    card.swap_status = not card.swap_status
    card.save()
    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=card.catalogue_id)
    card_info =  Catalogue.objects.get(id=card.catalogue_id)
    return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})
