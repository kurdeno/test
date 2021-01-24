from rest_framework import serializers
from datetime import date
from .models import *
from django.contrib.auth.models import User


def dlugosc_nr_telefonu(tel):
    if len(tel) != 9:
        raise serializers.ValidationError("Nr telefonu musi być 9 cyfrowy.")
    return tel


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['pk','imie', 'nazwisko', 'email', 'nr_telefonu', 'url']



class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = ['pk','imie', 'nazwisko', 'pesel', 'email', 'nr_telefonu', 'url']



    def validate_pesel(self, pesel):
        if len(pesel) != 11:
            raise serializers.ValidationError("PESEL musi być 11 cyfrowy.")
        return pesel


class ZamowienieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zamowienie
        fields = ['pk','status', 'data', 'klient', 'pracownik', 'url']



    def validate_data(self, d):
        if d > date.today():
            raise serializers.ValidationError("Data zamówieania nie może być w przyszłości.")
        return d


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['pk','nazwa', 'cena', 'url']



    def validate_cena(self, cena):
        if cena < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return cena


class ProduktSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produkt
        fields = ['pk','ilosc', 'oferta', 'zamowienie', 'url']



    def validate_ilosc(self, ilosc):
        if ilosc < 0:
            raise serializers.ValidationError("Ilosc nie może być ujemna.")
        return ilosc


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username','url']
