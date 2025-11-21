from django import forms
from .models import Yorum, Iletisim # <-- Iletisim'i eklemeyi unutma!
from django.contrib.auth.models import User # <-- Bunu eklemeyi unutma

# Yorum Formu (Zaten vardı)
class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['isim', 'icerik', 'puan'] # <-- 'puan' eklendi
        widgets = {
            'isim': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'icerik': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yorumunuzu buraya yazın...', 'rows': 3}),
            # Puan için 1-10 arası seçim kutusu
            'puan': forms.Select(choices=[(i, f'{i} Puan') for i in range(1, 11)], attrs={'class': 'form-select bg-dark text-white border-secondary'}),
        }

        

# --- YENİ EKLENEN: İLETİŞİM FORMU ---
class IletisimForm(forms.ModelForm):
    class Meta:
        model = Iletisim
        fields = ['isim', 'email', 'mesaj']
        widgets = {
            'isim': forms.TextInput(attrs={'class': 'form-control bg-black text-white border-secondary', 'placeholder': 'Adınız Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-black text-white border-secondary', 'placeholder': 'ornek@email.com'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control bg-black text-white border-secondary', 'rows': 4, 'placeholder': 'Bize ne söylemek istersiniz?'}),
        }


# --- KULLANICI BİLGİLERİ GÜNCELLEME FORMU ---
class KullaniciGuncellemeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] # Kullanıcı neleri değiştirebilsin?
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-black text-white border-secondary', 'placeholder': 'Adınız'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-black text-white border-secondary', 'placeholder': 'Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-black text-white border-secondary', 'placeholder': 'Email Adresiniz'}),
        }