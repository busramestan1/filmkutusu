# 🎬 FilmKutusu - Dinamik Sinema ve Etkileşim Platformu

**FilmKutusu**, kullanıcıların güncel sinema verilerini keşfedebildiği, film detaylarını inceleyebildiği ve içerisindeki oyunlaştırma (gamification) modülleriyle eğlenerek puan toplayabildiği Full-Stack bir web uygulamasıdır. 

🌐 **Canlı Demo:** [busramstn.pythonanywhere.com](https://busramstn.pythonanywhere.com)

---

## 🚀 Öne Çıkan Özellikler

* **🔎 Akıllı Canlı Arama (Live Search):** Kullanıcı arama çubuğuna yazarken sonuçların JavaScript ve AJAX ile anlık olarak, şık bir açılır menüde getirilmesi.
* **🎮 Oyunlaştırma ve Liderlik Tablosu:** * **Modunu Bul:** Kullanıcının ruh haline göre anlık film önerisi yapan algoritma.
  * **Sine-Bilgi & Emoji Bil:** Tarayıcı tabanlı mini bilgi yarışmaları. Doğru cevaplarla XP (Puan) kazanma.
  * **Top 10 Liderler:** Kazanılan puanlara göre kullanıcıların birbiriyle rekabet ettiği dinamik sıralama tablosu.
* **🏆 Tüm Zamanların En İyileri:** Kullanıcı oylarıyla belirlenen ve puan/eklenme tarihine göre dinamik sıralanan "Top 10" film listesi.
* **🤖 Otomatik Veri Çekme (Web Scraping/API):** Özel yazılmış Django Management Command (`film_cek.py`) sayesinde TMDB API kullanılarak otomatik film verisi, afişi ve açıklaması çekme.
* **⚙️ Gelişmiş Yönetim Paneli:** `django-jazzmin` kütüphanesi ile özelleştirilmiş, modern ve kullanıcı dostu admin arayüzü.

---

## 🛠️ Kullanılan Teknolojiler

**Backend (Arka Uç):**
* Python 3.x
* Django 5.x (MVT Mimarisi)
* SQLite (Geliştirme Ortamı)

**Frontend (Ön Yüz):**
* HTML5 & CSS3
* Bootstrap 5 (Responsive Tasarım)
* JavaScript (ES6+, DOM Manipülasyonu, Fetch API)

---

## 💻 Kurulum (Projeyi Kendi Bilgisayarında Çalıştırmak İçin)

Projeyi kendi bilgisayarınızda (lokal ortamda) çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Projeyi Klonlayın:**
```bash
git clone [https://github.com/busramestan1/filmkutusu.git](https://github.com/busramestan1/filmkutusu.git)
cd filmkutusu
2. Sanal Ortam (Virtual Environment) Oluşturun ve Aktif Edin:

Bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
3. Gerekli Kütüphaneleri Yükleyin:
(Projede kullanılan kütüphanelerin yüklendiğinden emin olun)

Bash
pip install django django-jazzmin requests
4. Veritabanını Hazırlayın:

Bash
python manage.py makemigrations
python manage.py migrate
5. Sunucuyu Başlatın:

Bash
python manage.py runserver
Tarayıcınızda http://127.0.0.1:8000/ adresine giderek projeyi görüntüleyebilirsiniz.


<img width="1919" height="901" alt="Ekran görüntüsü 2026-02-26 135423" src="https://github.com/user-attachments/assets/ba375ef2-626e-452f-aa4e-c536e36101e8" />
<img width="1898" height="913" alt="Ekran görüntüsü 2026-02-26 135406" src="https://github.com/user-attachments/assets/38e14f0d-be7e-4b8a-90c1-7aec03b97cba" />
<img width="1917" height="905" alt="Ekran görüntüsü 2026-02-26 135353" src="https://github.com/user-attachments/assets/fcd7c238-019d-48bd-a449-cc717bb315b0" />
<img width="1887" height="790" alt="Ekran görüntüsü 2026-02-26 135341" src="https://github.com/user-attachments/assets/f4e3b6b0-78ed-491f-b6b8-570b985aecda" />


👤 Geliştirici
Büşra Mestan


















