import numpy as np
from PIL import Image

image = Image.open("inicjaly.bmp")

# Informacje o obrazie
print(f"Tryb: {image.mode}")
print(f"Rozmiar: {image.size}")
print(f"Format: {image.format}")

# Tablica obrazu
image_arr = np.asarray(image)
image_arr = image_arr * 1

# Zapis tablicy obrazu do pliku
with open("inicjaly.txt", 'w') as file:
    for rows in image_arr:
        for item in rows:
            file.write(str(item) + ' ')
        file.write('\n')

# Informacje o tablicy obrazu
print()
print(f"Typ danych: {image_arr.dtype}")
print(f"Rozmiar tablicy: {image_arr.shape}")
print(f"Liczba elementów tablicy: {image_arr.size}")
print(f"Wymiar tablicy: {image_arr.ndim}")
print(f"Rozmiar wyrazu tablicy: {image_arr.itemsize}")
print(f"Piksel (50, 30): {image_arr[30][50]}")
print(f"Piksel (90, 40): {image_arr[40][90]}")
print(f"Piksel (99, 0): {image_arr[0][99]}")

# Wczytanie tablicy obrazu z pliku
loaded_arr = np.loadtxt("inicjaly.txt", dtype=np.bool_)


print("\n---- Tablica wczytana z pliku (bool_) ----")
print(f"Typ danych: {loaded_arr.dtype}")
print(f"Rozmiar tablicy: {loaded_arr.shape}")
print(f"Liczba elementów tablicy: {loaded_arr.size}")
print(f"Wymiar tablicy: {loaded_arr.ndim}")
print(f"Rozmiar wyrazu tablicy: {loaded_arr.itemsize}")
print(f"Piksel (50, 30): {loaded_arr[30][50]}")
print(f"Piksel (90, 40): {loaded_arr[40][90]}")
print(f"Piksel (99, 0): {loaded_arr[0][99]}")

loaded_arr = np.loadtxt("inicjaly.txt", dtype=np.uint8)

print("\n---- Tablica wczytana z pliku (uint8_) ----")
print(f"Typ danych: {loaded_arr.dtype}")
print(f"Rozmiar tablicy: {loaded_arr.shape}")
print(f"Liczba elementów tablicy: {loaded_arr.size}")
print(f"Wymiar tablicy: {loaded_arr.ndim}")
print(f"Rozmiar wyrazu tablicy: {loaded_arr.itemsize}")
print(f"Piksel (50, 30): {loaded_arr[30][50]}")
print(f"Piksel (90, 40): {loaded_arr[40][90]}")
print(f"Piksel (99, 0): {loaded_arr[0][99]}")

image_from_arr = Image.fromarray(loaded_arr)
image_from_arr.show()