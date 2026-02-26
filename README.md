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
📸 Ekran Görüntüleri
<img width="1919" height="901" alt="Ekran görüntüsü 2026-02-26 135423" src="https://github.com/user-attachments/assets/094ac05e-2477-490f-8381-ba0c5940b40a" />
<img width="1898" height="913" alt="Ekran görüntüsü 2026-02-26 135406" src="https://github.com/user-attachments/assets/1e81c853-cf83-47dc-95ff-0fae1f89ec85" />
<img width="1917" height="905" alt="Ekran görüntüsü 2026-02-26 135353" src="https://github.com/user-attachments/assets/7e28cf69-f8cc-4a02-a245-692e265bc7db" />
<img width="1887" height="790" alt="Ekran görüntüsü 2026-02-26 135341" src="https://github.com/user-attachments/assets/30b61136-6893-47e8-b170-ad062f074e60" />
<img width="1358" height="908" alt="Ekran görüntüsü 2026-02-26 140140" src="https://github.com/user-attachments/assets/402d188f-08ea-4790-8d5e-b83591955995" />
<img width="1364" height="903" alt="Ekran görüntüsü 2026-02-26 140128" src="https://github.com/user-attachments/assets/dd24994b-fff1-49af-97a5-21fcc3a1ed42" />
<img width="1896" height="898" alt="Ekran görüntüsü 2026-02-26 140042" src="https://github.com/user-attachments/assets/f2b9dfee-a798-4b56-8137-9f04a5693378" />

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



👤 Geliştirici
Büşra Mestan
















