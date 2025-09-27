# sefruit shop
https://farrel-rifqi-footballshop.pbp.cs.ui.ac.id/

# Tugas 2
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

# Tugas 3
## Alasannya diperlukan data delivery dalam pengimplementasian sebuah platform

## XML vs JSON, dan alasan JSON lebih populer

## Fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut

## Alasannya dibutuhkan csrf_token saat membuat form di Django

## Implementasi checklist step-by-step
### Menambah 4 fungsi views baru (XML, JSON)
1. show_xml()
2. show_json()
3. show_xmlbyid()
4. show_jsonbyid()
semua ditambahkan pada views.py
### Membuat routing URL untuk 4 fungsi views
menambah routing url xml, json dll pada urlpatterns di urls.py
### Membuat halaman data objek model
1. Buat base.html sebagai "template" pada ~/templates/. 
2. Ini digunakan untuk semua html pada ~/main/templates/. 
3. Update main.html 
3. 1. Tombol "Add" >> create_product.html
3. 2. If logic dan For loop logic untuk menampilkan product_list
3. 3. Tombol "Detail" >> product_details.html
### Membuat halaman form
1. Membuat forms.py untuk menambahkan product
2. Membuat create_product.html untuk menjalankan forms.py
3. Update views.py dengan func create_product()
4. Routing url pada urls.py
### Membuat halaman detail dari data
1. Membuat product_details.html
2. Update views.py dengan func show_product()
3. Routing url pada urls.py
### Mengakses 4 URL dengan Postman



### Github
```bash
git add .
git commit Tugas 3
git push pws master`
```
## Feedback untuk Asdos Tutorial 2
Asdos membantu ketika saya kewalahan. Salut!
