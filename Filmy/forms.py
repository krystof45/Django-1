from django.forms import ModelForm
from .models import Film,DodatkowInf,Ocena,Rezyser

class FilmForm(ModelForm):
    class Meta:
        model=Film
        field=['tytul','opis','premiera','rok','imdb_rating','okladka']
        exclude=()


class DodatkowInfForm(ModelForm):
    class Meta:
        model = DodatkowInf
        field = ['czas_trwania','gatunek']
        exclude = ()


class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        field = ['gwiazki','kometaz']
        exclude = ()



class RezyserForm(ModelForm):
    class Meta:
        model = Rezyser
        field = ['imie','nazwisko']
        exclude = ()