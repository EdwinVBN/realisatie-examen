from django.contrib import admin
from django.urls import path
from .views import User, Klant, Eigenaar

urlpatterns = [
    path('login/', User.login, name='login'),
    path('register/', Klant.register, name='register'),
    path('', User.home, name='home'),
    path('logout/', User.logout, name='logout'),
    path('profile/', User.profiel, name='profile'),
    path('planning/', Klant.planning, name='planning'),
    path('planning/<int:id>/', Klant.lesinfo, name='lesinfo'),
    path('lespakket/', Klant.lespakket, name='lespakket'),
    path('beheer/', Eigenaar.beheer, name='beheer'),
    path('beheer/<int:id>/', Eigenaar.profile_details, name='profile_details'),
    path('beheer/<int:id>/edit/', Eigenaar.profile_details_edit, name='profile_details_edit'),
    path('beheer/<int:id>/deactivate/', Eigenaar.deactivateren, name='profile_deactivate'),
    path('beheer/<int:id>/activate/', Eigenaar.activateren, name='profile_activate'),
    path('autos/', Eigenaar.autos, name='autos'),
    path('autos/<int:id>/', Eigenaar.auto_details, name='auto_details'),
    path('autos/<int:id>/edit/', Eigenaar.auto_edit, name='auto_edit'),
    path('autos/create/', Eigenaar.auto_create, name='auto_create'),
    path('autos/<int:id>/delete/', Eigenaar.auto_delete, name='auto_delete'),
]
