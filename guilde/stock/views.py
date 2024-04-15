from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from stock.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GameInstance
from django.views import generic
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import get_user
from datetime import datetime, timedelta


def index(request):
    template = loader.get_template("stock/index.html")
    return HttpResponse(template.render(request=request))


def infojeu(request, jeu_id):
    jeu = Game.objects.get(id=jeu_id)
    imgjeu = jeu.image
    descjeu = jeu.description
    urljeu = jeu.image
    nomjeu = jeu.name
    template = loader.get_template("./stock/infojeu.html")
    rendu = {'imgjeu': imgjeu, 'descjeu': descjeu,
             'nomjeu': nomjeu, 'bool': False, 'urljeu': urljeu}

    if Comment.objects.filter(game=jeu_id).exists():
        rendu['bool'] = True

        liste_commentaire = Comment.objects.filter(game=jeu_id)
        rendu['nbr_commentaires'] = int(len(liste_commentaire))

        for i in range(1, len(liste_commentaire)+1):
            commentaire = liste_commentaire[i-1]
            commentaires = commentaire.comments
            user_id = commentaire.user.id
            auteur = User.objects.get(id=user_id)
            nom = auteur.first_name
            prenom = auteur.last_name

            rendu['nom'+str(i)] = nom
            rendu['prenom'+str(i)] = prenom
            rendu['commentaires'+str(i)] = commentaires
    return HttpResponse(template.render(rendu))


def js(request):
    # Query videos games from database
    per_page = int(request.GET.get("per_page", 100))
    page = int(request.GET.get("page", 1))

    limit = per_page
    offset = (page - 1) * per_page

    games = Game.objects.filter(category="Jeu de société")[offset:offset+limit]

    games_list = Game.objects.filter(category="Jeu de société")
    paginator = Paginator(games_list, per_page)

    try:
        games = paginator.page(page)
    except EmptyPage:
        # Si la page demandée est supérieure à la dernière page possible, affichez la dernière page.
        games = paginator.page(paginator.num_pages)

    template = loader.get_template("stock/index_jeux_de_société.html")
    return HttpResponse(template.render({'games': games}, request=request))


def jv(request):
    # Query videos games from database
    per_page = int(request.GET.get("per_page", 100))
    page = int(request.GET.get("page", 1))

    limit = per_page
    offset = (page - 1) * per_page

    games = Game.objects.filter(category="Jeu vidéo")[offset:offset+limit]
    games_list = Game.objects.filter(category="Jeu vidéo")
    paginator = Paginator(games_list, per_page)

    try:
        games = paginator.page(page)
    except EmptyPage:
        # Si la page demandée est supérieure à la dernière page possible, affichez la dernière page.
        games = paginator.page(paginator.num_pages)

    template = loader.get_template("stock/index_jeux_video.html")
    return HttpResponse(template.render({'games': games}, request=request))


def jr(request):
    # Query videos games from database
    per_page = int(request.GET.get("per_page", 100))
    page = int(request.GET.get("page", 1))

    limit = per_page
    offset = (page - 1) * per_page

    games = Game.objects.filter(category="Jeu de rôle")[offset:offset+limit]
    games_list = Game.objects.filter(category="Jeu de rôle")
    paginator = Paginator(games_list, per_page)

    try:
        games = paginator.page(page)
    except EmptyPage:
        # Si la page demandée est supérieure à la dernière page possible, affichez la dernière page.
        games = paginator.page(paginator.num_pages)

    template = loader.get_template("stock/index_jeux_de_role.html")
    return HttpResponse(template.render({'games': games}, request=request))


def contact(request):
    template = loader.get_template("./stock/contact.html")
    return HttpResponse(template.render(request=request))


def search(request):
    requete = request.GET.get('query', 'not found')
    if requete == "":
        return index(request)

    per_page = int(request.GET.get("per_page", 100))
    page = int(request.GET.get("page", 1))

    limit = per_page
    offset = (page - 1) * per_page

    all_games = Game.objects.all()
    selected_games = [
        game.id for game in all_games if requete.lower() in game.name.lower()]
    games = Game.objects.filter(id__in=selected_games)[offset:offset+limit]
    template = loader.get_template("stock/index_recherche.html")
    return HttpResponse(template.render({'games': games}, request=request))


class LoanedGamesByUserListView(LoginRequiredMixin, generic.ListView):
    model = GameInstance
    template_name = './stock/gameinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            GameInstance.objects.filter(borrower=self.request.user)
            .filter(state__exact='o')
            .order_by('echeance')
        )


def resa(request, jeu_id):
    jeu = Game.objects.get(id=jeu_id)
    descjeu = jeu.description
    nomjeu = jeu.name
    urljeu = jeu.image
    template = loader.get_template("./stock/resa.html")
    return HttpResponse(template.render({'jeu_id': jeu_id, 'descjeu': descjeu, 'nomjeu': nomjeu, 'urljeu': urljeu}, request=request))


def BookingDate(request, jeu_id):

    # S'il s'agit d'une requête POST, traiter les données du formulaire.
    if request.method == 'POST':
        date = request.POST["from_date"]
        game = Game.objects.get(id=jeu_id)
        game_instance = GameInstance.objects.filter(game=game, disponibility = 'DISPONIBLE')[0]

        book = Booking()
        book.gameinstance = game_instance
        book.from_date = date
        book.to_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(weeks=4)
        user = request.user 
        book.user = user

        book.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'templates/stock/resa.html', context)
