from django.contrib import admin
from .models import Film,DodatkowInf,Ocena,Rezyser

# Register your models here.
#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields=['tytul','opis']
    #exclude = ['opis']
    list_display = ['tytul','imdb_rating','rok']
    list_filter = ['rok','imdb_rating']
    search_fields = ['tytul','opis']

admin.site.register(DodatkowInf)
admin.site.register(Ocena)
admin.site.register(Rezyser)