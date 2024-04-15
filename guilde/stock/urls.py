"""
URL configuration for guilde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, path
import stock.views
import stock.models

urlpatterns = [
    path('jv/<int:jeu_id>/', stock.views.infojeu, name='infojv'),
    path('jr/<int:jeu_id>/', stock.views.infojeu, name='infojr'),
    path('js/<int:jeu_id>/', stock.views.infojeu, name='infojs'),
    path('js', stock.views.js, name='cat_js'),
    path('jv', stock.views.jv, name='cat_jv'),
    path('jr', stock.views.jr, name='cat_jr'),
    path('contact', stock.views.contact, name='contact'),
    path('jv/<int:jeu_id>/resa/', stock.views.resa, name='infojv'),
    path('jr/<int:jeu_id>/resa/',stock.views.resa, name='infojr'),
    path('js/<int:jeu_id>/resa/',stock.views.resa, name='infojs'),
    path('jr/<int:jeu_id>/resa/book/', stock.views.BookingDate, name='bookjr'),
    path('jv/<int:jeu_id>/resa/book/', stock.views.BookingDate, name='bookjv'),
    path('js/<int:jeu_id>/resa/book/', stock.views.BookingDate, name='bookjs'),
    path('mygames/', stock.views.LoanedGamesByUserListView.as_view(), name='my_games'),
    path('search', stock.views.search, name='recherche'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
