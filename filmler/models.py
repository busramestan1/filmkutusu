from django.db import models
from django.contrib.auth.models import User

# --- FİLM MODELİ ---
class Film(models.Model):
    KATEGORILER = (
        ('Aksiyon', 'Aksiyon'),
        ('Komedi', 'Komedi'),
        ('Bilim Kurgu', 'Bilim Kurgu'),
        ('Dram', 'Dram'),
        ('Korku', 'Korku'),
    )
    isim = models.CharField(max_length=100)
    konu = models.TextField()
    resim = models.CharField(max_length=300, default="https://via.placeholder.com/300")
    puan = models.IntegerField(default=0)
    tur = models.CharField(max_length=50, choices=KATEGORILER, default='Aksiyon')
    yonetmen = models.CharField(max_length=100, default="", blank=True)
    oyuncular = models.CharField(max_length=300, default="", blank=True)

    def __str__(self):
        return self.isim

# --- YORUM MODELİ ---
class Yorum(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='yorumlar')
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    isim = models.CharField(max_length=50, verbose_name='İsim', default="Misafir")
    icerik = models.TextField(verbose_name='Yorumunuz')
    tarih = models.DateTimeField(auto_now_add=True)
    puan = models.IntegerField(default=10, verbose_name='Puanın')
    def __str__(self):
        return f"{self.isim} - {self.film.isim}"

# --- İLETİŞİM MODELİ ---
class Iletisim(models.Model):
    isim = models.CharField(max_length=100, verbose_name='Ad Soyad')
    email = models.EmailField(verbose_name='Email Adresi')
    mesaj = models.TextField(verbose_name='Mesaj')
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isim

# --- PROFİL MODELİ (GÜNCELLENMİŞ) ---
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puan = models.IntegerField(default=0)
    avatar = models.CharField(max_length=300, default="https://cdn-icons-png.flaticon.com/512/149/149071.png")
    
    # 👇 YENİ EKLENEN SATIR: İzleme Listesi (Bir sürü film tutabilir)
    izleme_listesi = models.ManyToManyField(Film, blank=True, related_name='listeye_alanlar')

    def __str__(self):
        return self.user.username