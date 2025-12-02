import requests
import time
from django.core.management.base import BaseCommand
from filmler.models import Film

class Command(BaseCommand):
    help = 'TMDB sitesinden sadece YENİ ve KONUSU DOLU filmleri çeker (Eskileri güncellemez)'

    def handle(self, *args, **kwargs):
        API_KEY = "4d7244e6a03280704c54ceb3202b3ee6" 
        
        tur_eslesmesi = {
            28: 'Aksiyon', 12: 'Aksiyon', 35: 'Komedi',
            878: 'Bilim Kurgu', 14: 'Bilim Kurgu',
            18: 'Dram', 27: 'Korku', 53: 'Korku',
            10749: 'Dram', 9648: 'Korku'
        }

        toplam_eklenen = 0
        
        # Taranmasını istediğiniz sayfa aralığını giriniz (1-20 1. sayfadan 20. sayfaya kadar olan filmleri tarar)
        BASLANGIC_SAYFA = 101  #en son  100 sayfayı taradı
        BITIS_SAYFA = 120

        self.stdout.write(f"--- Tarama Başlıyor: Sayfa {BASLANGIC_SAYFA} ile {BITIS_SAYFA} arası ---")

        for sayfa in range(BASLANGIC_SAYFA, BITIS_SAYFA + 1):
            self.stdout.write(f"--- Sayfa {sayfa} taranıyor... ---")
            
            URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=tr-TR&page={sayfa}"
            
            try:
                response = requests.get(URL, timeout=10)
                if response.status_code != 200:
                    self.stdout.write(self.style.ERROR(f"Sunucu Cevap Vermedi: Sayfa {sayfa}"))
                    continue

                data = response.json()

                for item in data.get('results', []):
                    # 1. KONTROL: Konu boşsa alma
                    konu = item.get('overview', "")
                    if not konu: continue 

                    tmdb_id = item['id']
                    baslik = item['title']

                    # 2. KONTROL: Veritabanında zaten varsa detay çekmekle uğraşma, direkt geç (HIZLANDIRICI)
                    if Film.objects.filter(isim=baslik).exists():
                        # self.stdout.write(f"Zaten var: {baslik}") # İstersen bu satırı açıp görebilirsin
                        continue

                    # --- Sadece Yeni Filmse Buradan Sonrası Çalışır ---
                    
                    puan = int(item['vote_average'])
                    poster_path = item.get('poster_path')
                    resim_url = f"https://image.tmdb.org/t/p/w342{poster_path}" if poster_path else "https://via.placeholder.com/300"

                    genre_ids = item.get('genre_ids', [])
                    film_turu = 'Dram' 
                    if genre_ids:
                        film_turu = tur_eslesmesi.get(genre_ids[0], 'Dram')

                    # Detay Çekimi (Yönetmen vs.)
                    try:
                        detay_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}/credits?api_key={API_KEY}&language=tr-TR"
                        detay_resp = requests.get(detay_url, timeout=5)
                        yonetmen = "Bilinmiyor"
                        oyuncular_str = ""
                        
                        if detay_resp.status_code == 200:
                            detay_data = detay_resp.json()
                            for crew in detay_data.get('crew', []):
                                if crew['job'] == 'Director':
                                    yonetmen = crew['name']
                                    break
                            oyuncular_list = [cast['name'] for cast in detay_data.get('cast', [])[:3]]
                            oyuncular_str = ", ".join(oyuncular_list)
                    except Exception:
                        yonetmen = "Bilinmiyor"
                        oyuncular_str = ""

                    # KAYDET (get_or_create mantığı)
                    Film.objects.create(
                        isim=baslik,
                        konu=konu, 
                        resim=resim_url, 
                        puan=puan,
                        tur=film_turu, 
                        yonetmen=yonetmen, 
                        oyuncular=oyuncular_str
                    )
                    
                    toplam_eklenen += 1
                    self.stdout.write(self.style.SUCCESS(f"✅ Yeni Eklendi: {baslik}"))

            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Bağlantı sorunu, 3 sn bekleniyor..."))
                time.sleep(3)
                continue

        self.stdout.write(self.style.SUCCESS(f'\nİŞLEM TAMAM! TOPLAM {toplam_eklenen} YENİ FİLM EKLENDİ! 🚀'))


    #python manage.py film_cek bu kod ile film çekiyoruz.
    