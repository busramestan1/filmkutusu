from django.contrib import admin
from .models import Film, Yorum, Iletisim, Profil

# --- FİLM YÖNETİMİ ---
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('isim', 'tur', 'puan', 'yonetmen')
    search_fields = ('isim', 'yonetmen', 'oyuncular')
    list_filter = ('tur', 'puan')
    list_per_page = 20

# --- YORUM YÖNETİMİ ---
@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('isim', 'film', 'tarih', 'kisa_icerik')
    search_fields = ('isim', 'icerik', 'film__isim')
    list_filter = ('tarih',)

    def kisa_icerik(self, obj):
        return obj.icerik[:50] + "..." if len(obj.icerik) > 50 else obj.icerik
    kisa_icerik.short_description = 'Yorum İçeriği'

# --- İLETİŞİM MESAJLARI YÖNETİMİ ---
@admin.register(Iletisim)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('isim', 'email', 'tarih')
    search_fields = ('isim', 'email', 'mesaj')
    readonly_fields = ('isim', 'email', 'mesaj', 'tarih')
    ordering = ('-tarih',)

# --- PROFİL YÖNETİMİ (AVATAR EKLENDİ) ---
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    # Listede görünecekler (Sütunlar)
    list_display = ('user', 'puan', 'avatar') 
    # İçine girince düzenlenebilecekler (Kutucuklar)
    fields = ['user', 'puan', 'avatar']