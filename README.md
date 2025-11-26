# 📚 Aplikasi Sistem Informasi Perpustakaan – UAS Pemrograman

Aplikasi Sistem Informasi Perpustakaan ini dikembangkan sebagai kebutuhan yang terjadi di lapangan. Sistem ini dirancang untuk membantu proses pengelolaan data perpustakaan secara lebih efektif, terstruktur, dan modern. Dengan memanfaatkan bahasa pemrograman Python serta antarmuka grafis Tkinter, aplikasi ini memungkinkan pengguna untuk melakukan berbagai aktivitas, seperti login, pengelolaan buku, pencatatan transaksi peminjaman, hingga menampilkan laporan kegiatan perpustakaan.  

Selain itu, aplikasi ini terhubung dengan database MySQL sehingga seluruh data dapat tersimpan dengan aman dan dapat diakses kembali kapan pun dibutuhkan. Penggunaan database juga memastikan integritas data serta memudahkan proses pencarian, perubahan, dan penghapusan data dalam jumlah besar. Aplikasi ini memiliki dua jenis pengguna, yaitu **Admin** dan **User**, masing-masing dengan hak akses dan fungsi yang berbeda sesuai kebutuhan operasional perpustakaan.

---

## 🎯 Tujuan Pengembangan

Tujuan utama pengembangan aplikasi ini adalah untuk menciptakan sebuah sistem sederhana namun fungsional yang dapat digunakan sebagai contoh implementasi dari konsep pemrograman terapan, manajemen database, serta pemahaman mengenai sistem informasi perpustakaan. Dengan adanya aplikasi ini, diharapkan proses pengolahan data perpustakaan dapat dilakukan secara lebih cepat, akurat, dan efisien.

---

## 🚀 Fitur Utama Aplikasi

### 🔐 **1. Sistem Login**
Aplikasi dilengkapi dengan halaman login yang berfungsi untuk memvalidasi identitas pengguna. Sistem dapat membedakan antara pengguna berstatus **Admin** dan **User**, kemudian mengarahkan mereka ke halaman utama sesuai hak akses masing-masing. Proses login ini juga memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses sistem.

### 👤 **2. Halaman User**
File: `tabUser.py`  
Pengguna dengan status User dapat menggunakan aplikasi untuk:
- Melihat daftar buku yang tersedia di perpustakaan  
- Mengecek informasi detail tentang buku  
- Melakukan permintaan peminjaman buku  
- Melihat riwayat dan status peminjaman  

Fitur ini dirancang agar memudahkan anggota perpustakaan dalam memperoleh informasi secara lebih cepat tanpa harus bertanya secara manual kepada petugas.

### 🛠 **3. Halaman Admin**
File: `tabAdmin.py`  
Admin memiliki akses yang lebih luas untuk mengelola data. Fitur yang tersedia meliputi:
- Mengelola data buku (menambah, mengubah, dan menghapus buku)  
- Mengelola data pengguna perpustakaan  
- Mengontrol dan memverifikasi transaksi peminjaman maupun pengembalian buku  
- Melihat laporan kegiatan perpustakaan dalam jangka waktu tertentu  

Fitur ini membantu petugas perpustakaan dalam menjaga kerapian data sekaligus mempermudah proses administrasi sehari-hari.

### 🗄 **4. Database MySQL**
File: `perpustakaan.sql`  
Aplikasi ini terhubung dengan database MySQL yang berisi tabel buku, tabel pengguna, dan tabel transaksi peminjaman. Struktur database dirancang agar sederhana namun tetap memenuhi kebutuhan dalam memproses data perpustakaan. Seluruh data yang diinput melalui aplikasi akan masuk ke database dan dapat diolah kembali sesuai kebutuhan.

---

## 🛠 Teknologi & Tools yang Digunakan

- **Python 3.x** – bahasa utama untuk mengembangkan logika aplikasi  
- **Tkinter** – library Python untuk membangun antarmuka grafis  
- **MySQL / MariaDB** – penyimpanan data perpustakaan  
- **Pillow (PIL)** – digunakan untuk menampilkan gambar/logo dalam aplikasi  
- **Git** – manajemen versi kode proyek  

---

## 📦 Cara Instalasi Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/username/nama-repo.git
cd UAS pemograman
2. Install Dependensi Python
bash
Salin kode
pip install pillow
pip install mysql-connector-python
3. Import Database
Buka phpMyAdmin atau MySQL Client

Buat database baru, misalnya:

nginx
Salin kode
perpustakaan
Import file:

pgsql
Salin kode
perpustakaan.sql
4. Sesuaikan Konfigurasi Database
Pastikan file Python menggunakan konfigurasi yang sesuai:

python
Salin kode
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)
5. Jalankan Aplikasi
bash
Salin kode
python loginpustaka.py
📂 Struktur Folder Proyek
nginx
Salin kode
UAS pemograman/
├── loginpustaka.py
├── tabAdmin.py
├── tabUser.py
├── perpustakaan.sql
├── logo.png
└── README.md
🎓 Penutup
Aplikasi Sistem Informasi Perpustakaan ini dibuat sebagai implementasi nyata yang dibutuhkan. Meskipun sederhana, aplikasi ini telah memenuhi kebutuhan dasar dari sebuah sistem pengelolaan perpustakaan. Pengembangan lebih lanjut masih sangat terbuka, seperti penambahan fitur pencarian, manajemen kategori buku, hingga integrasi dengan sistem online.

👩‍💻 Developer
Nama  : Rizka Permata Arianti
email : rizkapermataarianti@gmail.com

