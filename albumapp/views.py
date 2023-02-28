from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
import random


@login_required(login_url='landing')
def home(request):
    """     Vista de la página principal del usuario

        Se hace una petición al servidor para obtener todas las
        instancias del usuario. A este query se le indica que la información no
        muestre instancias duplicadas y las ordene respecto al campo catalogue_id

    Args:
        request (metodo http): Petición al servidor

    Returns:
        render: Renderea home.html en caso que el usuario esté autenticado y
                pasa un quesyset a modo para mostrar en el html 
    """
    user = request.user
    user_distinct_cards = Album.objects.filter(user_id=user).values(
        'catalogue_id', 'catalogue_id__messier', 'catalogue_id__name',
        'catalogue_id__image').distinct().order_by('catalogue_id')    
    return render(request, 'home.html', {'cards': user_distinct_cards})


def random_catalogue_instance(_model):
    return _model.objects.get(pk=random.randrange(1, _model.objects.count()))


@login_required(login_url='landing')
def adquire_new_card(request):   
    """     Vista de la página de adquisición de nueva carta

        Si el servidor recibe una petición con el método POST, se le asigna una
        nueva instancia del modelo Album al usuario.

        Se hace uso de 3 funciones: 
        - random_catalogue_instance, la cual selecciona una instancia aleatoria
            del modelo Catalogue y retorna esta. Esta función se encuentra fuera
        - save_album_instance, la cual crea una nueva instancia del modelo Album.
        - get_card_info, la cual obtiene la información del modelo Catalogue a
            partir de la llave foránea catalogue_id del modelo Album

    Args:
        request (metodo http): Petición al servidor

    Retunrs:
        render: Renderea new_card.html en caso de que el usuario esté autenticado.
                Si la petición fue POST, se incluye la información de la instancia
                Catalogue
    """    

    def save_album_instance(user, random_messier):
        new_card = Album(user_id=user.id, catalogue_id=random_messier.id, swap_status=False)
        new_card.save()
        return new_card

    def get_card_info(new_card):
        card_info = Album.objects.filter(pk=new_card.id).values(
            'catalogue_id__messier', 'catalogue_id__name', 'catalogue_id__type',
            'catalogue_id__ar', 'catalogue_id__dec', 'catalogue_id__dist', 
            'catalogue_id__description', 'catalogue_id__image' )
        return card_info

    if request.method == 'POST':
        user = request.user
        random_messier = random_catalogue_instance(Catalogue)
        new_card = save_album_instance(user, random_messier)
        new_card_info = get_card_info(new_card)
        return render(request, 'new_card.html', { 'card': new_card_info[0] })
    
    return render(request, 'new_card.html')

@login_required(login_url='landing')
def card_info(request, id):
    """     Vista de la página de información de la carta

        Se obtiene la información astronómica de la carta (instancia del modelo 
        Catalogue), para mostrar al usuario

    Args:
        request (método http):  Petición al servidor
        id (int):   Valor entero de la llave primaria del modelo Catalogue

    Returns:
        render: Renderea card_info.html, además se incluye la información de la
                instancia Catalogue
    """
    card_info = Catalogue.objects.get(id=id)   
    return render(request, 'card_info.html', { 'card': card_info })


@login_required(login_url='landing')
def swap_card(request, id):
    """     Vista de la página de instancias album del usuario para una misma 
            instancia del módelo Catalgoue
        
        Se hace una petición al servidor para obtener todas las instancias del
        usuario que contengan la misma llave en el campo catalogue_id
        En otras palabras, a partir de la llave catalogue_id se obtienen todas
        las cartas "repetidas" que tiene el usuario.

    Args:
        request (metodo http): Petición al servidor del
        id (int): Valor entero de la llave primaria del modelo Catalogue, que a
                su vez es llave foránea en el modelo Album

    Returns:
        render: Renderea swap_card.html, junto con la información de la instancia
                Catalogue y las instancias Album con el mismo catalogue_id
    """
    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=id)
    card_info =  Catalogue.objects.get(id=id)
    return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})

@login_required(login_url='landing')
def delete_card(request, id):
    """     Función para borrar una instancia del modelo Album

        Esta función elimina la instancia del modelo Album con la llave primaria 
        (id) que es recibida en la petición al servidor.
        En caso de que aún se tengan más instancias con la misma llave fóranea
        catalogue_id se renderea de nuevo swap_card.html con la información de las
        instancias, en caso de ya no existir instancia alguna con el valor id
        en el campo catalogue_id se redireciona al usuario a home (home.html)

    Args:
        request (metodo http): Petición al servidor
        id (int): Llave primaria de la instancia Album

    Returns:
        render: Renderea swap_card.html junto con la información de las instancias
                del usuario con el mismo catalgoue_id. En caso de no existir
                instancias redirije a home (home.html)
    """ 
    card = Album.objects.get(id=id)
    card.delete()
    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=card.catalogue_id)
    if user_cards:
        card_info =  Catalogue.objects.get(id=card.catalogue_id)
        return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})
    else:
        return redirect('home')

def change_swap_status(card):
    card.swap_status = not card.swap_status
    card.save()

@login_required(login_url='landing')
def swap_status_card(request, id):
    """     Función para cambiar el status de intercambio de una instancia Album

        Esta función cambia el valor booleano del campo swap_status de una 
        instancia Album del usuario.
        El cambio del estado booleano se realiza mediante la función change_swap_status
        la cual niega el status actual de este campo

    Args:
        request (metodo http): Peticón al servidor
        id (int): Llave primaria de una instancia del modelo Album

    Returns:
        render: Renderea swap_card.html, junto con los campos de las instancias
                Album del usuario
    """
    
    card = Album.objects.get(id=id)
    change_swap_status(card)

    user_cards = Album.objects.filter(user_id=request.user.id).filter(catalogue_id=card.catalogue_id)
    card_info =  Catalogue.objects.get(id=card.catalogue_id)
    return render(request, 'swap_card.html', {'cards': user_cards, 'card_info': card_info})
