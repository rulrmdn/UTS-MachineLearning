import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'fakultas': ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"],
    'jumlah_mahasiswa': [260, 28, 284, 465, 735],
    'akreditasi': ["A", "A", "B", "A", "A"]
}

info_mahasiswa = pd.DataFrame(data)
print(info_mahasiswa)

plt.figure(figsize=(10, 6))
gambar = sns.barplot(data=info_mahasiswa, x='fakultas', y='jumlah_mahasiswa', palette='viridis')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.show()
