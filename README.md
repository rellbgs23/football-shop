# sefruit shop
https://farrel-rifqi-footballshop.pbp.cs.ui.ac.id/

## Implementasi Checklist
### Membuat projek Django baru
1. Set up python environment
   ```bash
   python -m venv env
   env\Scripts\activate
2. Buat projek django dan aplikasi baru
   ```bash
   django-admin startproject football_shop
### Menambahkan aplikasi main
1. Membuat aplikasi main
   ```bash
   python manage.py startapp main
2. Menambahkan main pada INSTALLED_APPS di settings.py
### Routing projek
1. Membuat main.html pada ~\main\templates (buat dir templates juga)
2. Membuat dan mengatur views.py
3. Membuat dan mengatur urls.py pada ~\main dan ~\football_shop
### Model pada aplikasi main
1. Mengatur models.py
2. Migrasi model
   ```bash
   python manage.py makemigrations
   python manage.py migrate
### Upload ke PWS
1. Upload app dengan git
2. Mengatur settings.py untuk memberi akses
3. Mengatur environment pada PWS

## Bagan request client ke web
HTTP Request > urls.py > views.py > models.py > main.html > views.py > HTTP Response

## Peran settings.py
settings.py berperan untuk mengatur DATABASES, INSTALLED_APPS, MIDDLEWARE, dan ALLOWED_HOSTS.

## Cara kerja migrasi database di django
1. Django membuat file migrasi setelah membaca perubahan di models.py
   ```bash
   python manage.py makemigrations
2. Django mengubah models.py dan menyinkronkan dengan database
   ```bash
   python manage.py migrate

## Alasan Django menjadi intro ke software development
Django menggunakan python, bahasa high level yang cepat dimengerti. Terlebih lagi, Django memiliki fitur-fitur yang cukup dan bersifat 'lengkap'.

## Feedback untuk Asdos Tutorial 1
Tutorial sudah sangat lengkap, bahkan untuk setiap contoh sudah terdapat penjelasan yang cukup mendalam. Salut!
