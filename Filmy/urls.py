
from django.urls import path
from Filmy.views import Wszystkie_filmy,nowy_film,edytuj_film,usun_film

urlpatterns = [

    path('wszystkie/',Wszystkie_filmy,name="Wszystkie_filmy"),
    path('nowy/',nowy_film,name="nowy_film"),
    path('edytuj/<int:id>/',edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/',usun_film,name="usun_film")

]