import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Örnek veri seti (daha fazla boyutlu veri)
data = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
    [10, 11, 12, 13]
])

# 1. Adım: Veriyi standardize et
mean = np.mean(data, axis=0)
standardized_data = data - mean

# 2. Adım: Kovaryans matrisi oluştur
cov_matrix = np.cov(standardized_data, rowvar=False)

# 3. Adım: Kovaryans matrisinin öz değerlerini ve öz vektörlerini hesapla
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)

# 4. Adım: En büyük öz değerlere göre sıralama yap
sorted_indices = np.argsort(eigen_values)[::-1]  # Büyükten küçüğe sırala
eigen_values = eigen_values[sorted_indices]
eigen_vectors = eigen_vectors[:, sorted_indices]

# 5. Adım: Boyut azaltma (örneğin, 2 veya 3 bileşene indir)
num_components = 3  # İlk 3 bileşeni seç
selected_vectors = eigen_vectors[:, :num_components]

# 6. Adım: Veriyi yeni uzaya projekte et
reduced_data = np.dot(standardized_data, selected_vectors)

# Çıktı: İndirgenmiş veri
print("İndirgenmiş Veri (PCA Sonucu):")
print(reduced_data)

# 2D Görselleştirme (İlk 2 bileşen)
plt.figure(figsize=(8, 6))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='blue', edgecolor='k')
plt.title("PCA ile Boyut İndirgeme (2D)")
plt.xlabel("1. Temel Bileşen")
plt.ylabel("2. Temel Bileşen")
plt.grid()
plt.show()

# 3D Görselleştirme (İlk 3 bileşen)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(reduced_data[:, 0], reduced_data[:, 1], reduced_data[:, 2], c='blue', edgecolor='k')
ax.set_title("PCA ile Boyut İndirgeme (3D)")
ax.set_xlabel("1. Temel Bileşen")
ax.set_ylabel("2. Temel Bileşen")
ax.set_zlabel("3. Temel Bileşen")
plt.show()
