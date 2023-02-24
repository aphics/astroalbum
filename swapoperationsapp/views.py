from django.shortcuts import render
from albumapp.models import Album
from django.contrib.auth.models import User
from .models import SwapOperations
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='landing')
def swap_pool(request):
    
    user_cards_swap = Album.objects.filter(user_id=request.user).filter(swap_status=1).values(
        'id', 'user_id', 'catalogue_id', 'catalogue_id__name', 'catalogue_id__image').order_by('catalogue_id')
    other_cards_swap = Album.objects.exclude(user_id=request.user).filter(swap_status=1).values(
        'id', 'user_id', 'catalogue_id', 'catalogue_id__name', 'catalogue_id__image').order_by('catalogue_id')
                
    if request.method == 'POST':

        user_card_id = request.POST.get('user_card_id')
        other_card_id = request.POST.get('other_card_id')

        user_card = Album.objects.get(id=user_card_id)
        other_card = Album.objects.get(id=other_card_id)
        
        if user_card_id and other_card_id:
            swap_operation = SwapOperations(
                emissor_user = User.objects.get(username=user_card.user),
                emissor_album = Album.objects.get(id=user_card.id),
                receptor_user = User.objects.get(username=other_card.user),
                receptor_album = Album.objects.get(id=other_card.id),
            )
            print(swap_operation.emissor_user)
            swap_operation.save()
            user_card.user, other_card.user = other_card.user, user_card.user
            user_card.swap_status = 0
            other_card.swap_status = 0
            user_card.save()
            other_card.save()


            # swap_operation = SwapOperations()
            return render(request, 'swap_pool.html', {
                'msg_warning': '¡Felicidades, tu intercambio se realizó con éxito!',
                'msg_color': 'text-green-500',
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'status_button': 'enabled'
            })        
        elif user_card_id == None and other_card_id != None:
            return render(request, 'swap_pool.html', {
                'msg_warning': '¡Cuidado: No seleccionaste ninguna carta tuya!',
                'msg_color': 'text-red-500',
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'status_button': 'enabled'
            })
        elif user_card_id != None and other_card_id == None:
            return render(request, 'swap_pool.html', {
                'msg_warning': '¡Cuidado: No seleccionaste ninguna carta de la pila de intercambio!',
                'msg_color': 'text-red-500',
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'status_button': 'enabled'
            })
        elif user_card_id == None and other_card_id == None:
            return render(request, 'swap_pool.html', {
                'msg_warning': '¡Cuidado: No seleccionaste ninguna carta de tus intercambios \
                    ni la pila de intercambio!',
                'msg_color': 'text-red-500',
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'status_button': 'enabled'
            })

    elif user_cards_swap.count() > 0 and other_cards_swap.count() > 0:
        return render(request, 'swap_pool.html', 
            {
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'status_button': 'enabled'
            })

    elif user_cards_swap.count() > 0 and other_cards_swap.count() == 0 :
        return render(request, 'swap_pool.html',
            {
                'user_cards': user_cards_swap, 
                'msg_other': 'No hay cambios disponibles',
                'status_button': 'disabled',
                'cursor_status': 'cursor-not-allowed'
            })

    elif user_cards_swap.count() == 0 and other_cards_swap.count() > 0 :
        return render(request, 'swap_pool.html',
            {
                'msg_user': 'No tienes cartas disponibles',
                'other_cards': other_cards_swap,
                'status_button': 'disabled',
                'cursor_status': 'cursor-not-allowed'
            })

    elif user_cards_swap.count() == 0 and other_cards_swap.count() == 0 :
        return render(request, 'swap_pool.html',
            {
                'msg_user': 'No tienes cartas disponibles',
                'msg_other': 'No hay cartas disponibles',
                'status_button': 'disabled',
                'cursor_status': 'cursor-not-allowed'
            })

    return render(request, 'swap_pool.html')