from django.db import models

# Create your models here.
#

class DodatkowInf(models.Model):
     Gatunek= {
         (0,'Inne'),
         (1, 'Akcji'),
         (2, 'Historyczny'),
         (3, 'Sci-fi')
     }

     czas_trwania = models.PositiveSmallIntegerField(default=0)
     gatunek = models.PositiveSmallIntegerField(default=0,choices=Gatunek)


class Film(models.Model):
    tytul=models.CharField(max_length=64,blank=False,unique=True)
    rok=models.PositiveSmallIntegerField(default=2000)
    opis=models.TextField(default='')
    premiera=models.DateField(null=True,blank=True)
    imdb_rating = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    okladka=models.ImageField(upload_to='okladki',null= True,blank=True)

    dodatkowe = models.OneToOneField(DodatkowInf,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return '{} ({})'.format(self.tytul,self.rok)

class Ocena(models.Model):
    kometaz=models.TextField(default="",blank=True)
    gwiazki =models.PositiveSmallIntegerField(default=0)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)

class Rezyser(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film,related_name="rezyserzy")