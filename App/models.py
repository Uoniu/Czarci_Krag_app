from django.db import models

# Create your models here.


class Test(models.Model):
    col = models.CharField(max_length=100)


class Test_Photos(models.Model):
    photo = models.ImageField(upload_to='test_photos')
    name = models.CharField(max_length=100)


class Aktualnosci(models.Model):
    Naglowek = models.CharField(max_length=50)
    Tresc = models.CharField(max_length=100)
    Istotnosc = models.IntegerField()


class FAQ (models.Model):
    Tytul = models.CharField(max_length=50)
    Tresc = models.CharField(max_length=200)
    Odpowiedz = models.CharField(max_length=200)


class Buty (models.Model):
    Rozmiar = models.IntegerField()
    Id_Rezerwacji = models.ForeignKey("Rezerwacja",on_delete=models.SET_NULL,null=True)


class Rezerwacja (models.Model):
    DataRozpoczecia = models.DateTimeField()
    DataZakonczenia = models.DateTimeField()
    IdUzytkownika = models.ForeignKey("Uzytkownik",on_delete=models.SET_NULL,null=True)
    Uwagi = models.CharField(max_length=50)
    IdUslugi = models.ForeignKey("Uslugi",on_delete=models.SET_NULL,null=True)


class Uslugi(models.Model):
    NazwaUslugi = models.CharField(max_length=30,null=False)
    TypUslugi = models.CharField(max_length=20)

    def __str__(self):
        return self.NazwaUslugi()

class Uzytkownik(models.Model):
    TypUzytkownika = models.CharField(max_length=20)
    Imie = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=80)
    Haslo = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    NrTelefonu = models.CharField(max_length=15)

class Galeria (models.Model):
    Tytul = models.CharField(max_length=30)
    Zdjecie = models.FileField()

class ProgramLojalnosciowy (models.Model):
    Nagroda = models.CharField(max_length=30)
    Punkty = models.IntegerField()
    IdUzytkownika = models.ForeignKey("Uzytkownik",on_delete=models.SET_NULL,null=True)
