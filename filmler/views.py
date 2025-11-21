from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Film, Yorum, Iletisim, Profil
from .forms import YorumForm, IletisimForm, KullaniciGuncellemeForm
from django.db.models import Avg # <-- Bunu en tepeye ekle


def anasayfa(request):
    # 1. Tüm filmleri çek
    tum_filmler = Film.objects.all().order_by('-id')
    
    # --- YENİ EKLENEN KISIM: SLIDER İÇİN İLK 5 FİLM ---
    slider_filmleri = tum_filmler[:5] 
    
    # Linkten gelen bilgileri al
    search_query = request.GET.get('q')
    kategori_query = request.GET.get('tur')
    
    uyari_mesaji = ""

    # --- FİLTRELEME MANTIĞI ---
    if search_query:
        tum_filmler = tum_filmler.filter(
            Q(isim__icontains=search_query) | Q(konu__icontains=search_query)
        )
        if not tum_filmler.exists():
            uyari_mesaji = f"Üzgünüz, '{search_query}' hakkında bir sonuç bulamadık. Ama bunları sevebilirsiniz 👇"
            tum_filmler = Film.objects.all().order_by('-id')[:4]

    elif kategori_query:
        tum_filmler = tum_filmler.filter(tur=kategori_query)
        if not tum_filmler.exists():
            uyari_mesaji = f"Henüz '{kategori_query}' kategorisinde filmimiz yok. Bunlara bakabilirsin 👇"
            tum_filmler = Film.objects.all().order_by('-id')[:4]

    # --- SAYFALAMA ---
    paginator = Paginator(tum_filmler, 3) 
    page_number = request.GET.get('page')
    filmler = paginator.get_page(page_number)

    return render(request, 'anasayfa.html', {
        'filmler': filmler,
        'slider_filmleri': slider_filmleri, # <-- HTML'e gönderiyoruz
        'uyari_mesaji': uyari_mesaji,
        'arama_kelimesi': search_query
    })

  # --- DETAY SAYFASI ---

def detay(request, id):
    film = get_object_or_404(Film, id=id)
    listede_mi = False
    form = YorumForm()
    
    if request.user.is_authenticated:
        if film in request.user.profil.izleme_listesi.all():
            listede_mi = True
    
    if request.method == 'POST':
        form = YorumForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.film = film 
            
            if request.user.is_authenticated:
                yorum.kullanici = request.user
                yorum.isim = request.user.username 
            
            yorum.save()
            
            # --- ORTALAMA PUAN HESAPLAMA ---
            # Bu filme yapılan tüm yorumların puan ortalamasını al
            ortalama = Yorum.objects.filter(film=film).aggregate(Avg('puan'))['puan__avg']
            if ortalama:
                film.puan = int(ortalama) # Küsuratı at, tam sayı yap
                film.save()
            # -------------------------------

            messages.success(request, 'Yorumun ve Puanın kaydedildi! 🌟')
            return redirect('detay', id=id)
        else:
            messages.error(request, 'Lütfen alanları kontrol et.')

    benzer_filmler = Film.objects.filter(tur=film.tur).exclude(id=id).order_by('-puan')[:4]

    return render(request, 'detay.html', {
        'film': film, 
        'benzer_filmler': benzer_filmler,
        'form': form, 
        'listede_mi': listede_mi
    })



# --- YENİ SAYFALAR ---

def hakkinda(request):
    film_sayisi = Film.objects.count()
    yorum_sayisi = Yorum.objects.count()
    ekip_sayisi = 3 

    context = {
        'film_sayisi': film_sayisi,
        'yorum_sayisi': yorum_sayisi,
        'ekip_sayisi': ekip_sayisi
    }
    return render(request, 'hakkinda.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajınız başarıyla gönderildi! En kısa sürede döneceğiz. 🚀')
            return redirect('iletisim')
    else:
        form = IletisimForm()

    return render(request, 'iletisim.html', {'form': form})

def en_iyiler(request):
    en_iyi_filmler = Film.objects.all().order_by('-puan')[:10]
    return render(request, 'en_iyiler.html', {'filmler': en_iyi_filmler})


# --- ÜYELİK SİSTEMİ ---

def kayit_ol(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profil.objects.create(user=user) # Profil oluştur
            login(request, user)
            messages.success(request, 'Aramıza hoşgeldin! 🎉')
            return redirect('anasayfa')
    else:
        form = UserCreationForm()
    return render(request, 'kayit.html', {'form': form})

def giris_yap(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # --- YÖNETİCİ KONTROLÜ ---
            if user.is_superuser:
                messages.success(request, 'Hoşgeldin Patron! Admin paneline yönlendiriliyorsun. 😎')
                return redirect('/admin/') # Yöneticiyi direkt panele at
            # -------------------------

            return redirect('anasayfa') # Normal üyeyi ana sayfaya at
    else:
        form = AuthenticationForm()
    return render(request, 'giris.html', {'form': form})
def cikis_yap(request):
    logout(request)
    messages.info(request, 'Başarıyla çıkış yapıldı. Yine bekleriz! 👋')
    return redirect('anasayfa')

@login_required(login_url='giris_yap')
def profil(request):
    profil, created = Profil.objects.get_or_create(user=request.user)
    
    # --- FORM İŞLEMLERİ ---
    if request.method == 'POST':
        
        # 1. Durum: Profil Resmi Güncelleme (Eski kodumuz)
        if 'avatar_link' in request.POST:
            yeni_avatar = request.POST.get('avatar_link')
            if yeni_avatar:
                profil.avatar = yeni_avatar
                profil.save()
                messages.success(request, 'Profil fotoğrafın güncellendi! 😎')
                return redirect('profil')

        # 2. Durum: Kullanıcı Bilgileri Güncelleme (YENİ)
        elif 'bilgi_guncelle' in request.POST:
            user_form = KullaniciGuncellemeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Bilgilerin başarıyla güncellendi! ✅')
                return redirect('profil')

    else:
        # Sayfa ilk açıldığında formu mevcut bilgilerle doldur
        user_form = KullaniciGuncellemeForm(instance=request.user)

    # --- PUAN HESAPLAMA (Aynen Kalsın) ---
   # 👇 YENİ KOD: Eğer kullanıcı yönetici DEĞİLSE puanı hesapla
    if not request.user.is_superuser:
        yorum_sayisi = Yorum.objects.filter(kullanici=request.user).count()
        puan = yorum_sayisi * 50
        profil.puan = puan
        profil.save()
    
    # Yöneticiyse (is_superuser) burayı atlar ve
    # veritabanında elle girdiğin puan neyse o kalır.

    # ... (Geri kalan kodlar aynı) ...
    puan = profil.puan # Puanı profilden al
    
    # ... (Önceki kodlar aynı) ...

    # İlerleme Çubuğu (Hedef 2000 puan olsun ki bar hemen dolmasın)
    bar_yuzdesi = int((puan / 2000) * 100) 
    if bar_yuzdesi > 100: bar_yuzdesi = 100

    # --- YENİ ROZET SİSTEMİ (200 PUAN ARALIKLI) ---
    rozet = "Çaylak İzleyici 🍿"
    rozet_renk = "secondary" # Gri
    
    if puan >= 200:
        rozet = "Patlamış Mısır Canavarı 🌽"
        rozet_renk = "info" # Mavi
    if puan >= 400:
        rozet = "Sinema Tutkunu 🎥"
        rozet_renk = "purple" # mor
    if puan >= 600:
        rozet = "Film Eleştirmeni 🧐"
        rozet_renk = "success" # Yeşil
    if puan >= 800:
        rozet = "Başrol Oyuncusu 🌟"
        rozet_renk = "warning text-dark" # Sarı
    if puan >= 1000:
        rozet = "Yönetmen Koltuğu 📣"
        rozet_renk = "danger" # Kırmızı
    if puan >= 1200:
        rozet = "Yapımcı 💰"
        rozet_renk = "light text-dark" # Beyaz
    if puan >= 1400:
        rozet = "Sinema Efsanesi 👑"
        rozet_renk = "dark border border-warning" # Siyah+Altın Çerçeve

    # ... (Geri kalan kodlar aynı) ...

    yorumlar = Yorum.objects.filter(kullanici=request.user).order_by('-tarih')

    context = {
        'profil': profil,
        'puan': puan,
        'bar_yuzdesi': bar_yuzdesi,
        'rozet': rozet,
        'rozet_renk': rozet_renk,
        'yorumlar': yorumlar,
        'user_form': user_form # <-- Formu HTML'e gönderdik
    }
    return render(request, 'profil.html', context)

@login_required(login_url='giris_yap')
def listeye_ekle_cikar(request, id):
    film = get_object_or_404(Film, id=id)
    profil = request.user.profil
    
    # Eğer film zaten listedeyse -> ÇIKAR
    if film in profil.izleme_listesi.all():
        profil.izleme_listesi.remove(film)
        messages.warning(request, f'{film.isim} listenden çıkarıldı. 🗑️')
    # Yoksa -> EKLE
    else:
        profil.izleme_listesi.add(film)
        messages.success(request, f'{film.isim} listene eklendi! ➕')
        
    # Geldiğin sayfaya (Detay sayfasına) geri dön
    return redirect('detay', id=id)