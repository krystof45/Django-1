from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Film,DodatkowInf,Ocena
from .forms import FilmForm,DodatkowInfForm,OcenaForm,RezyserForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,FilmSerializer


class UserView(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset= Film.objects.all()
    serializer_class = FilmSerializer
# Create your views here.

def Wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    #return HttpResponse('<h1>To jest pierwszy test</h1>')
    return render(request,'Filmy.html',{'filmy':wszystkie})
@login_required
def nowy_film(request):
    nowy=False
    form_film= FilmForm(request.POST or None,request.FILES or None)
    form_dodatkowy= DodatkowInfForm(request.POST or None)
    form_rezyser= RezyserForm(request.POST or None)

    if all((form_film.is_valid(),form_dodatkowy.is_valid(),form_rezyser.is_valid())):
        film=form_film.save(commit=False)
        dodatkowe=form_dodatkowy.save()
        rezyserzy=form_rezyser.save()
        film.dodatkowe=dodatkowe
        film.rezyserzy=rezyserzy
        form_film.save()
        return redirect(Wszystkie_filmy)

    return render(request,'nowy_film.html',{'form':form_film,'form_dod':form_dodatkowy,'form_rez':form_rezyser,'w_bazie':nowy})
@login_required
def edytuj_film(request,id):
    nowy = True
    film= get_object_or_404(Film,pk=id)
    oceny= Ocena.objects.filter(film=film)
    rezyserzy=film.rezyserzy.all()
    try:
        dodatkowe= DodatkowInf.objects.get(film=film.id)
    except DodatkowInf.DoesNotExist:
        dodatkowe=None



    form_film = FilmForm(request.POST or None, request.FILES or None,instance=film)
    form_dodatkowy = DodatkowInfForm(request.POST or None,instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)
    form_rezyser = RezyserForm(request.POST or None)

    if request.method =='POST':
        if 'gwiazki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film=film
            ocena.save()

    if all((form_film.is_valid(), form_dodatkowy.is_valid(),form_rezyser.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowy.save()
        rezyserzy = form_rezyser.save()
        film.dodatkowe = dodatkowe
        film.rezyserzy = rezyserzy
        form_film.save()
        return redirect(Wszystkie_filmy)


    return render(request, 'nowy_film.html', {'form': form_film,'form_dod':form_dodatkowy,'form_rez':form_rezyser,'oceny':oceny,'form_oceny':form_ocena,'w_bazie':nowy})
@login_required
def usun_film(request,id):
    film= get_object_or_404(Film,pk=id)

    if request.method=="POST":
        film.delete()
        return redirect(Wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})