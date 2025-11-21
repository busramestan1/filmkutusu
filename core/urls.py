from django.contrib import admin
from django.urls import path
from filmler.views import (
 anasayfa, detay, hakkinda, iletisim, en_iyiler,
 kayit_ol, giris_yap, cikis_yap, profil,listeye_ekle_cikar
)
urlpatterns = [
    path('admin/', admin.site.urls),
    # Anasayfa için de isim verelim, lazım olur
    path('', anasayfa, name='anasayfa'),
    # İŞTE DÜZELTİLMESİ GEREKEN SATIR 👇
    path('film/<int:id>/', detay, name='detay'),
    
    path('hakkinda/', hakkinda, name='hakkinda'),
    path('iletisim/', iletisim, name='iletisim'),
    path('en-iyiler/', en_iyiler, name='en_iyiler'),
    path('kayit/', kayit_ol, name='kayit_ol'),
    path('giris/', giris_yap, name='giris_yap'),
    path('cikis/', cikis_yap, name='cikis_yap'),
    path('profil/', profil, name='profil'),
    path('liste-islem/<int:id>/', listeye_ekle_cikar, name='liste_islem'),
]