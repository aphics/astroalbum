from django.shortcuts import render, redirect
from albumapp.models import Album
from django.contrib.auth.models import User
from .models import SwapOperations
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='landing')
def swap_pool(request):
    """     Vista de zona de intercambio del usuario

        - Método GET:
        Esta función obtiene las instancias con status de intercambiable 
        (swap_status = 1), tanto del usuario (user_card_swap) como de los demás
        usuarios (other_cards_swap).
        Si en la respuesta de los querysets, al menos uno está vacío, desactiva 
        el botón que realiza el método POST. En caso de que ambos querysets NO 
        estén vacíos, activa el botón que envía el método POST.
        En ambos casos se pasan ambos querysets al render para mostrar su información.

        - Método POST:
        La petición al servidor con el método POST se lleva a cabo cuando el
        usuario acciona el botón de intercambio.

        Primero se ejecuta una sentencia try para obtener del método POST el 
        valor de la llave primaria de la instancia del usuario y la llave 
        primaria de la instancia de la pila de intercambio. Si el bloque no arroja
        error, se manda a llamar la función make_swap, la cual realiza el
        intercambio (Se detalla su comportamiento en su definición).

        Si el bloque try arroja un error se procede a renderizar de nuevo el
        html, pero se le arroja un mensaje de advertencia al usuario. Este error
        se debe a que el usuario no seleccionó la carta propia (instancia propia) 
        a intercambiar o la carta de la pila de intercambio (instancia de otro usuario)
        o ambas cartas, pero dió click al botón de realizar intercambio

    Args:
        request (metodo http): Petición al servidor para

    Returns:
        render: Dependiendo
    """

    def make_swap(user_card, other_card):
        """     Función que realiza el intercambio de propietario de instancias Album

        La función recibe la intancia Album del usuario en sesión y la instancia
        Album del otro usuario. Crea una instancia en el modelo SwapOperations 
        con los campos correspondientes.
        Posteriormente se realiza un intercambio de los valores en los campos user
        en cada instancia de Album. Ademá, en ambas instancias se cambia el status
        de swap_status por False (0). Por último, se guardan estos cambios

        Args:
            user_card (Album instance): Instancia Album del usuario en sesión
            other_card (Album instance): Instancia Album del otro usuario
        """
        swap_operation = SwapOperations(
                emissor_user = User.objects.get(username=user_card.user),
                emissor_album = Album.objects.get(id=user_card.id),
                receptor_user = User.objects.get(username=other_card.user),
                receptor_album = Album.objects.get(id=other_card.id),
            )
        swap_operation.save()
        user_card.user, other_card.user = other_card.user, user_card.user
        user_card.swap_status = 0
        other_card.swap_status = 0
        user_card.save()
        other_card.save()
        
    
    user_cards_swap = Album.objects.filter(user_id=request.user).filter(swap_status=1).values(
        'id', 'user_id', 'catalogue_id', 'catalogue_id__name', 'catalogue_id__image').order_by('catalogue_id')
    other_cards_swap = Album.objects.exclude(user_id=request.user).filter(swap_status=1).values(
        'id', 'user_id', 'catalogue_id', 'catalogue_id__name', 'catalogue_id__image').order_by('catalogue_id')
                
    if request.method == 'POST':
        user_card_id = request.POST.get('user_card_id')
        other_card_id = request.POST.get('other_card_id')

        try:
            user_card = Album.objects.get(id=user_card_id)
            other_card = Album.objects.get(id=other_card_id)
            make_swap(user_card, other_card)
            return redirect('swap_pool')     
        except:
            return render(request, 'swap_pool.html', {
                'msg_warning': 'Selecciona una carta tuya y una de la pila de intercambio',
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

    else:
        return render(request, 'swap_pool.html',
            {
                'user_cards': user_cards_swap, 
                'other_cards': other_cards_swap,
                'msg_warning': 'No hay intercambios disponibles',
                'msg_color': 'text-red-500',
                'status_button': 'disabled',
                'cursor_status': 'cursor-not-allowed'
            })
