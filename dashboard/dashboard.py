import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("datafix.csv")  # Sesuaikan path dataset
    return df

df = load_data()

# Mapping bulan
month_map = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}

# Judul Dashboard
st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚴")

# Membuat tab
tab1, tab2, tab3 = st.tabs(["Summary", "🚴‍♂️ Fitur Perbandingan Bulanan", "☁️ Analisis Pengaruh Cuaca"])

#Sidebar untuk rentang bulan
with st.sidebar:
    selected_tab = st.radio("Pilih Fitur", ["Fitur Perbandingan Bulanan"], index=0)
    
    if selected_tab == "Fitur Perbandingan Bulanan":
        # Sidebar untuk memilih rentang bulan
        st.sidebar.header("🔍 Filter Data")
        selected_year = st.sidebar.radio("Pilih Tahun", options=[2011, 2012])

    # Menggunakan select_slider agar bulan bisa tampil dalam format nama bulan
    start_month, end_month = st.sidebar.select_slider(
        "Pilih Rentang Bulan",
        options=list(month_map.keys()),  # Gunakan angka bulan sebagai pilihan
        format_func=lambda x: month_map[x],  # Tampilkan dalam format nama bulan
        value=(1, 12)  # Default: Januari - Desember
        
)
    filtered_df = df[
    (df["yr"] == selected_year) & 
    (df["mnth"] >= start_month) & 
    (df["mnth"] <= end_month)
]
 
# Tab 1: Summary
with tab1:
    st.subheader("📅 Tren Penyewaan Sepeda per Bulan (2011 vs 2012)")
    monthly_agg = df.groupby(["yr", "mnth"])['cnt'].sum().reset_index()
    monthly_agg["Tahun"] = monthly_agg["yr"]
    monthly_agg["Bulan"] = monthly_agg["mnth"]
    
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(data=monthly_agg, x="Bulan", y="cnt", hue="Tahun", marker="o", palette=["blue", "red"], ax=ax)
    ax.set_title("📊 Tren Penyewaan Sepeda per Bulan (2011 vs 2012)")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_xticks(range(1,13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
    ax.legend(title="Tahun")
    ax.grid(True)
    st.pyplot(fig)

    st.subheader("🚴‍♂️ Penyewaan Sepeda: Hari Kerja vs Akhir Pekan per Tahun")
    workday_agg = df.groupby(["yr", "workingday"])['cnt'].sum().reset_index()
    workday_agg["Tahun"] = workday_agg["yr"]
    workday_agg["Hari Kerja (1=Ya, 0=Tidak)"] = workday_agg["workingday"]
    
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(data=workday_agg, x="Hari Kerja (1=Ya, 0=Tidak)", y="cnt", hue="Tahun", palette=["blue", "red"], ax=ax)
    ax.set_title("🚴‍♂️ Penyewaan Sepeda: Hari Kerja vs Akhir Pekan (2011 vs 2012)")
    ax.set_xlabel("Hari Kerja (0=Akhir Pekan, 1=Hari Kerja)")
    ax.set_ylabel("Total Penyewaan Sepeda")
    ax.set_xticks(ticks=[0,1])
    ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
    ax.legend(title="Tahun")
    st.pyplot(fig)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Scatter Plot Suhu, Kelembapan, Kecepatan Angin vs Penyewaan Sepeda
    st.subheader("🌤️ Hubungan Cuaca dan Penyewaan Sepeda")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    sns.scatterplot(x=df['temp'], y=df['cnt'], ax=axes[0], color='blue')
    axes[0].set_title("Suhu vs Penyewaan Sepeda")
    axes[0].set_xlabel("Suhu Terstandarisasi")
    axes[0].set_ylabel("Jumlah Penyewa Sepeda")

    sns.scatterplot(x=df['hum'], y=df['cnt'], ax=axes[1], color='green')
    axes[1].set_title("Kelembapan vs Penyewaan Sepeda")
    axes[1].set_xlabel("Kelembapan")
    axes[1].set_ylabel("Jumlah Penyewa Sepeda")

    sns.scatterplot(x=df['windspeed'], y=df['cnt'], ax=axes[2], color='red')
    axes[2].set_title("Kecepatan Angin vs Penyewaan Sepeda")
    axes[2].set_xlabel("Kecepatan Angin Terstandarisasi")
    axes[2].set_ylabel("Jumlah Penyewa Sepeda")
    
    st.pyplot(fig)
plt.show()

# Tab 2: Perbandingan Bulanan
with tab2:

    if selected_tab == "Fitur Perbandingan Bulanan":
        st.subheader(f"📅 Perbandingan Penyewaan Sepeda dari {month_map[start_month]} hingga {month_map[end_month]} {selected_year}")
        
        # Agregasi jumlah penyewa berdasarkan kategori hari dalam rentang bulan
        agg_data = filtered_df.groupby("weekday_type")["cnt"].sum().reset_index()
        
        # Visualisasi Bar Plot
        fig, ax = plt.subplots(figsize=(6,4))
        sns.barplot(x="weekday_type", y="cnt", data=agg_data, palette=["orange", "blue"])
        ax.set_xlabel("Kategori Hari")
        ax.set_ylabel("Jumlah Penyewa Sepeda")
        ax.set_title(f"Penyewaan Sepeda dari {month_map[start_month]} hingga {month_map[end_month]} {selected_year}")
        st.pyplot(fig)
        
        # Menampilkan jumlah total penyewa
        total_rentals = filtered_df["cnt"].sum()
        st.markdown(f"### 🚲 **Total Penyewaan Sepeda:** {total_rentals:,} sepeda dari {month_map[start_month]} hingga {month_map[end_month]} {selected_year}")

# Tab 3: Analisis Pengaruh Cuaca
with tab3:
    st.subheader(f"☁️ Analisis Pengaruh Cuaca terhadap Penyewaan Sepeda ({month_map[start_month]} - {month_map[end_month]} {selected_year})")

    # Scatter plot antara jumlah penyewaan dan faktor cuaca
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Faktor Cuaca yang Dianalisis
    weather_factors = ["temp", "hum", "windspeed"]
    titles = ["Suhu (°C) vs Penyewaan Sepeda", "Kelembapan (%) vs Penyewaan Sepeda", "Kecepatan Angin vs Penyewaan Sepeda"]
    colors = ["red", "blue", "green"]

    # Plot setiap faktor cuaca
    for i, (factor, title, color) in enumerate(zip(weather_factors, titles, colors)):
        row, col = divmod(i, 2)
        sns.scatterplot(data=filtered_df, x=factor, y="cnt", ax=axes[row, col], color=color, alpha=0.6)
        axes[row, col].set_title(title)
        axes[row, col].set_xlabel(factor)
        axes[row, col].set_ylabel("Jumlah Penyewaan Sepeda")

    # Hapus subplot kosong jika jumlah faktor kurang dari subplot
    fig.delaxes(axes[1, 1])

    # Tampilkan plot
    st.pyplot(fig)

    # Menampilkan Korelasi antara Cuaca dan Penyewaan Sepeda
    correlation_matrix = filtered_df[["cnt", "temp", "hum", "windspeed"]].corr()
    st.write("### 🔍 Korelasi antara Faktor Cuaca dan Penyewaan Sepeda")
    st.dataframe(correlation_matrix.style.background_gradient(cmap="coolwarm"))

    # Menambahkan Keterangan Cara Membaca Korelasi
    st.markdown("""
    **Cara Membaca Korelasi:**
    - **Nilai mendekati +1** → Hubungan positif yang kuat (misalnya, jika suhu naik, penyewaan cenderung naik).
    - **Nilai mendekati -1** → Hubungan negatif yang kuat (misalnya, jika kelembapan naik, penyewaan bisa turun).
    - **Nilai mendekati 0** → Tidak ada hubungan signifikan antara faktor cuaca dan jumlah penyewaan.
    """)
 