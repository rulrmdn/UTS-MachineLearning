import pandas as pd

# Data mahasiswa dan biaya harian
data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'Mahasiswa': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi'],
    'Datang': [2, 3, 4, 1, 2, 5, 2],
    'Biaya_per_datang': [30000, 35000, 25000, 15000, 20000, 30000, 35000]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menambahkan kolom Biaya_total
df['Biaya_total'] = df['Datang'] * df['Biaya_per_datang']

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
rata_rata_datang = df['Datang'].mean()
print(f"a) Rata-rata mahasiswa datang pada minggu ini: {rata_rata_datang:.2f}")

# b) Kapan biaya tertinggi terjadi?
biaya_tertinggi = df.loc[df['Biaya_total'].idxmax()]
print(f"b) Biaya tertinggi terjadi pada hari: {biaya_tertinggi['Hari']} dengan biaya: {biaya_tertinggi['Biaya_total']}")

# c) Hari apa biaya lebih dari 110000?
hari_biaya_lebih_110000 = df[df['Biaya_total'] > 110000]['Hari'].tolist()
print(f"c) Hari dengan biaya lebih dari 110000: {', '.join(hari_biaya_lebih_110000)}")

# d) Siapa yang paling banyak datang ke kampus?
mahasiswa_terbanyak_datang = df.groupby('Mahasiswa')['Datang'].sum().idxmax()
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {mahasiswa_terbanyak_datang}")

# e) Siapa yang datang pada hari minggu?
datang_minggu = df[df['Hari'] == 'Minggu']['Mahasiswa'].tolist()
print(f"e) Mahasiswa yang datang pada hari Minggu: {', '.join(datang_minggu)}")

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi_value = df['Biaya_total'].max()
biaya_terendah_value = df['Biaya_total'].min()
print(f"f) Biaya tertinggi: {biaya_tertinggi_value}, Biaya terendah: {biaya_terendah_value}")

# g) Berapa frekuensi datang tertinggi dan terendah?
datang_tertinggi_value = df['Datang'].max()
datang_terendah_value = df['Datang'].min()
print(f"g) Frekuensi datang tertinggi: {datang_tertinggi_value}, Frekuensi datang terendah: {datang_terendah_value}")
