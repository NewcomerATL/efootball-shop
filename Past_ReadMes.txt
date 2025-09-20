// ReadMe_Tugas2

# Tugas 2
# eFootball-shop
# Kolaborator: Jonathan Hans Emanuelle

Nama : Anderson Tirza Liman

NPM : 2406355893

Kelas : PBP B

Tautan: https://anderson-tirza-efootballshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Jawab:
    Secara jujur, saya masih agak kesulitan dalam mengimplementasikan checklist, akan tetapi saya berhasil menavigasi kesulitan saya dan menyelesaikan tugas ini. 
    1. Pertama-tama, saya membuat sebuah repository di GitHub sebagai langkah awal. Saya menamai repository tersebut efootball-shop.
    2. Kemudian, karena saya sudah menginstall Django, saya kemudian membuat sebuah direktori baru untuk proyek ini, dan mengaktifkan virtual environent.
    3. Setelah itu, saya menyiapkan depemdencies dan menginstallnya agar bisa membuat sebuah proyek pada Django.
    4. Saya memulai proyek Django setelah semua requirements selesai diunduh
    5. Kemudian saya melakukan set up pada web PWS, mengatur environsnya beserta credentialsnya.
    6. Saya juga mengatur url yang akan dibuat. Saya hendak memastikan bahwa tahap ini membuahkan sebuah webpage yang menyatakan bahwa saya sudah berhasil.
    7. Setelah memastikan website bisa berjalan, saya membuat sebuah direktori baru bernama main.
    8. Pada main, saya melengkapi semua keperluannya, termasuk migrations dan templatenya untuk ditampilkan di webpage.
    9. Saya juga mengubah urls.py dengan menginclude "main.urls" agar routing bisa berjalan dengan baik, dan aplikasi main dapat tampak di webpage
    10. Models menjadi tahap yang patut dimodifikasi dalam tugas ini. Saya menambahkan beberapa hal di models.py saya, semua kebutuhan tugas saya masukkan: model bernama Product, atributnya antara lain: name, price, description, thumbail, category, dan is_featured. Adapun, saya juga menambahkan beberapa attribut lain, seperti stock dan rating. Category choices juga saya update dan sekarang ada beberapa pilihan.
    11. Tanpa kehadiran views.py, tampilan HTML yang saya buat tidak dapat tampil. Saya mengubah views.py pada direktori main dengan menambahkan identitas, dan mereturn request agar webpage dapat tampak
    12. Pada urls.py, saya menambahkan urlpatterns dan import show_main agar dapat memetakan fungsi yang telah dibuat di views.py, alias webpagenya benar-benar menampilkan tulisan identitas.
    13. Setelah selesai mengerjakan semua, saya melakukan git add, commit, dan push. Kemudian, saya juga melakukan test dan pengecekan deployment. Deployment berhasil dan webpage berhasil menampilkan judul proyek, nama, npm, dan kelas saya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Referensi gambar bagan, terinspirasi dari kolaborator, Jonathan Hans E.
    https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg (Link bagan, diambil dari tutorial/lab 1 di website: https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1/)
    Atau jika dirangkum,

    [Client Browser]
        │
        ▼  meminta request (Request dari user, misalnya untuk akses URL)
    urls.py (URLconf)
        │   Mencocokkan pola URL
        ▼
    views.py (View Function/Class)
        │  Menangani logika aplikasi
        │  bisa juga meminta data dari models.py (opsional)
        ▼
    models.py (Model)
        │  menangani Query / transaksi data ke database
        ▼
    Database 
        │ transaksi data
        ▼
    models.py 
        │ kembali ke views.py dengan hasil query
        ▼
    views.py 
        │  memilih template
        ▼
    templates/*.html (Template)
        │
        ▼
    [Client Browser] Response berupa halaman HTML ditampilkan

    Penjelasan:
    - urls.py
    * Berfungsi sebagai router.
    * Mencocokkan pola URL dari request client dengan fungsi/class view yang sesuai.

    - views.py
    * Menjadi perantara antara request client, model, dan template.
    * Bisa saja hanya mengembalikan HTML sederhana, atau mengambil data dari database melalui model. Setelah data siap, view akan memilih template yang tepat dan memberikan context data.

    - models.py
    * Mendefinisikan struktur data (tabel di database) serta interaksi dengan database menggunakan ORM Django.
    * View memanggil model ketika perlu menambah, mengambil, mengubah, atau menghapus data.
    * Data hasil query dikembalikan lagi ke view.

    - templates (HTML)
    * Bertugas menampilkan data dalam bentuk yang ramah pengguna.
    * Template menggunakan context dari view (misalnya {{ name }} atau {{ product_list }}) untuk di-render menjadi HTML akhir.
    * HTML ini kemudian dikirim sebagai response ke browser.

    - Database
    * Menyimpan data aplikasi secara persisten.
    * Django ORM pada models.py akan menerjemahkan instruksi Python menjadi query SQL yang dijalankan di database.
    * Memnungkinkan transaksi data dengan models.py

3. Jelaskan peran settings.py dalam proyek Django!
    File settings.py adalah pusat kendali utama dalam proyek Django. File ini pertama kali dibaca saat aplikasi dijalankan dan menentukan bagaimana seluruh komponen bekerja agar sinergi terbentuk dengan baik. Di dalamnya terdapat konfigurasi penting seperti kunci rahasia (SECRET_KEY), debug mode, daftar aplikasi (INSTALLED_APPS), middleware, database, lokasi template dan static file, hingga aturan keamanan.
    Tanpa settings.py, Django tidak dapat menentukan pilihan database, penentuan aplikasi yang aktif, bahkan daftar domain yang boleh mengakses. Berkas tersebut memastikan semua bagian bisa berjalan dengan aturan dan kesepakatan yang konsisten.
    settings.py adalah otak pengaturan proyek Django karena semua keputusan dasar tentang jalannya aplikasi, baik di tahap development maupun production, ditentukan olehnya.

4. Bagaimana cara kerja migrasi database di Django?
    Migrasi di Django adalah sebuah cara kerja atau mekanisme untuk menjaga struktur database agar selalu sesuai dengan definisi model pada models.py. Prosesnya cukup sederhana, yakni setiap kali ada perubahan pada model (terjadi penambahan data, atau perubahan tabel), Django akan mencatat perubahan itu ke dalam file migrasi menggunakan perintah makemigrations. File migrasi tersebut berisi instruksi yang menjelaskan apa saja perubahan yang harus dilakukan pada database.
    Ketika perintah migrate dijalankan, Django membaca file migrasi tersebut dan mengeksekusi instruksi SQL yang sesuai agar database diperbarui secara tepat. Dengan cara ini, developer tidak perlu menulis query SQL secara manual, melainkan cukup mengandalkan ORM Django yang mengubah model Python menjadi tabel database yang konsisten dan tertata.
    Migrasi dalam konteks Django adalah penghubung peubahan logika data dalam aplikasi dengan kode Pyhton (models.py) sehingga semua perubahan logika aplikasi up-to-date di databasenya.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena dua hal basic:
    Pertama, urusan bahasa. Bahasa yang dipakai Django adalah Python dengan penggunaannya yang relatif mudah, dipahami secara cepat oleh pemula, sintaks yang sederhana, tapi tetap kuat untuk building real projects.

    Kedua, menurut saya karena fitur Django yang lengkap dan supportif terhadap pemula. Framework Django sudah menyediakan hampir semua kebutuhan dasar web development, seperti routing, ORM Django, template engine, autentikasi, hingga admin panel.

    Dengan kombinasi keduanya, mahasiswa pemula atau developer baru bisa belajar konsep pengembangan aplikasi tanpa harus membangun semuanya dari nol. Django juga punya dokumentasi yang rapi dan komunitas besar, sehingga lebih ramah untuk dipelajari dibanding framework lain yang lebih kompleks bagi pemula.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Sebenarnya bagi saya untuk konten materi tidak masalah, akan tetapi saya juga mengharapkan pengajaran fundamental dari ajakan/langkah-langkah dalam tutorial, agar bisa coding yang paham akan tujuan.

// Readme Tugas 3
# Tugas 3
# eFootball-shop

Nama : Anderson Tirza Liman

NPM : 2406355893

Kelas : PBP B

Tautan: https://anderson-tirza-efootballshop.pbp.cs.ui.ac.id/

1.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah sebuah proses pengiriman data di antara berbagai komponen dalam sebuah platform. Data delivery diperlukan karena beberapa hal, antara lain:
a. Komunikasi, agar platform dapat fungsional melalui data yang dikirim dari pengguna ke sistem. Platform tidak berguna tanpa kehadiran data yang dapat di-input maupun dari yang di-output.
b. Sinkronisasi, yakni memastikan data tetap menjaga konsistensinya pada bagian-bagian platform.
c. Integrasi, agar memungkinkan sistem berinteraksi dengan banyak layanan lain, misalnya API pembayaran.
d. User experience, karena tanpa data delivery, user tidak akan dapat memperoleh informasi secara real-time (misalnya notifikasi).

Data delivery sangat diperlukan agar sebuah platform dapat bekerja secara fungsional, interaktif, dan dinamis.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Keduanya memiliki kelebihannya masing-masing. XML sendiri lebih kuat untuk data dengan struktur yang cukup rumit, mendukung skema validasi, namespace, dan metadata. Sementara itu, JSON sendiri lebih ringan, lebih human-readable, lebih cepat diproses oleh browser/JavaScript karena langsung bisa dipetakan ke objek.

JSON lebih populer dibandingkan XML karena beberapa hal, antara lain:
a. Sintaks lebih sederhana, ringkas, dan mudah dibaca
b. Lebih efisien untuk transmisi data jarena umumnya file JSON berukuran lebih kecil.
c. Dapat terintegrasi langsung dengan JavaScript.
d. Lebih cepat diproses pada modern API web (pada sebagian besar REST API menggunakan JSON).

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari form.is_valid() adalah memvalidasi data yang diinput serta dikirim user melalui form berdasarkan aturan-aturan yang telah didefinisikan oleh pengembang di Django Form (sebagai contoh, field type, panjang maksimal, required field, dan lain-lain).

form.is_valid() akan mengembalikan True jika input valid, kemudian data yang sudah dibersihkan dapat diakses melalui form.cleaned_data. Sebaliknya, jika tidak valid, form.is_valid() mengembalikan False, dan secara otomatis Django akan menyediakan pesan error yang bisa ditampilkan kepada user.

Method tersebut dibutuhkan sebagai upaya pencegahan wrong input/dangerous input. Wrong input misalnya seperti email tidak valid, password yang kosong. Dangerous input seperti SQL injection. Semua ini ditujukan untuk menghindari kerusakan data di database akibat input tidak sesuai format (input yang tidak valid).

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Forgery) adalah sebuah serangan ketika penyerang memanipulasi user agar tanpa sadar mengirimkan request ke website yang sudah terautentikasi. Penyerang dapat melegitimasi transfer uang, mengubah password, dan lain-lain.

Dalam sistem Django, ditambahkan sebuah mekanisme pertahanan, yakni csrf_token. Hal tersebut ditujukan untuk memastikan bahwa request benar-benar berasal dari halaman asli aplikasi milik kita sendiri, bukan dari website berbahaya.

Ada resiko dan konsekuensi apabila tidak menambahkan csrf_token, antara lain:
a. Website akan rentan terhadap serangan CSRF oleh penjahat siber.
b. Penyerang dapat menciptakan form palsu di website lain, secara diam-diam mengirimkan request ke server Django yang dimiliki dengan identitas user yang sedang login.
Sebagai contoh, pertama-tama user login ke aplikasi perbankan, kemudian membuka situs berbahaya. Situs tersebut berisi form tersembunyi yang secara otomatis mengirimkan request transfer uang. Ketika tidak ada csrf_token, server akan menganggap request tersebut valid. Ketika ada, pengguna selamat dari serangan CSRF.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Penambahan 4 fungsi dilakukan dengan menambahkan kode dan fungsi pada views.py. Perubahan besarnya ada pada penamaan dan pengambilan informasi dari kelas Product (kalau di tutorial, namanya news).
b. Kemudian melanjutkan dengan routing, yang terpenting ada di bagian urls.py. Ditambahkan import beserta path-nya. Hal ini agar semua dapat terhubung dan dapat digunakan dengan maksimal oleh pengguna nantinya.
c. Untuk pembuatan halaman utama, add product, dan detail, dinamikanya mirip seperti yang diajarkan di tutorial. Perlu dibuat base nya, kemudian disambung dengan halaman main, create, dan detailnya. Semuanya menggunakan block content. Pada proses ini, proses pembuatan html dipadukan dengan fungsi dan field yang telah dibuat di models dan views. Catatan besarnya adalah penggantian field-field sesuai dengan tugas 2, kemudian penggantian kata kunci "news" menjadi product. (Saya sendiri banyak error di sini karena lupa menggantinya). 
d. Termasuk juga halaman detail dan formnya, saya mengubah susunan form dan jenis inputnya, sehingga sesuai seperti layaknya football shop. Hal yang saya ganti kebanyakan adalah variabel news menjadi variabel product agar sesuai dengan apa yang dibuat. Beberapa fitur dari tutorial saya hapus karena tidak relevan.
e. Terakhir, saya membuat readme.md sebagai dokumentasi dan catatan mengenai pekerjaan saya.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Saya rasa tutorial sudah oke, yang perlu saya perbaiki adalah inisiatif saya untuk bertanya. Rasanya, saya kurang bertanya mengenai beberapa hal yang membuat saya agak bingung mengerjakan tugas ini.

![Screenshot akses Get XML](image.png)
![Screenshot akses Get JSON](image-1.png)
![Screenshot akses Get XML by ID](image-2.png)
![Screenshot akses Get JSON by ID](image-3.png)