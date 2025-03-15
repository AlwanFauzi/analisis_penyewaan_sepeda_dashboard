# 🚴‍♂️ Dashboard Analisis Penyewaan Sepeda  

Dashboard ini dikembangkan menggunakan **Streamlit** untuk menganalisis dan memvisualisasikan data penyewaan sepeda berdasarkan berbagai faktor lingkungan dan kondisi cuaca.  

## 📌 Fitur Dashboard  
✅ **Summary**: Menampilkan kesimpulan dari seluruh analisis yang dibuat  
✅ **Perbandingan Bulanan**: Analisis jumlah penyewaan sepeda dalam rentang bulan tertentu.  
✅ **Analisis Pengaruh Cuaca**: Visualisasi hubungan antara faktor cuaca (suhu, kelembapan, kecepatan angin) terhadap jumlah penyewaan sepeda.  
✅ **Filter Interaktif**: Memilih rentang bulan dan tahun untuk analisis yang lebih spesifik.  

# 📌 Cara Menjalankan Dashboard  
## 1️⃣ Clone Repository  
Jika belum memiliki kode, clone repository ini terlebih dahulu:

```bash
git clone https://github.com/AlwanFauzi/analisis_penyewaan_sepeda_dashboard.git
cd analisis_penyewaan_sepeda_dashboard
```

## 2️⃣ Siapkan Virtual Environment (Opsional tapi Direkomendasikan)  

```bash
conda create --name main-ds python=3.12
conda activate main-ds
```

## 3️⃣ Install Dependencies  
Pastikan semua dependensi sudah terinstal dengan menjalankan perintah:

```bash
pip install -r requirements.txt
```

## 4️⃣ Jalankan Aplikasi Streamlit  

```bash
streamlit run dashboard.py
```

🚀 Aplikasi akan berjalan di [http://localhost:8501](http://localhost:8501)
