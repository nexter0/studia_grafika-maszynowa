import numpy as np
from PIL import Image


C: (int, int, int) = (0, 255, 255)
M: (int, int, int) = (255, 0, 255)
Y: (int, int, int) = (255, 255, 0)
K: (int, int, int) = (0, 0, 0)

def rysuj_pasy_pionowe_szare(width: int, height: int, grub: int) -> Image:

    arr_size: (int, int, int) = (height, width, 3)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości pasów.")

    obraz_arr = np.zeros(arr_size, dtype=np.uint8)

    # Przejdź po tablicy z krokiem grub
    step = 0
    for x in range(0, width, grub):
        for y in range(height):
            # Ustaw punkty od (x, y) do (x + grub, y) tak, aby
            # każdy kolejny pasek był o 10% jaśniejszym odcieniem szarości, aż do białego
            # i zapętlaj
            obraz_arr[y, x:x + grub] = ((25.5 * step) % 255, (25.5 * step) % 255, (25.5 * step) % 255)
        step += 1

    return Image.fromarray(obraz_arr)


def generuj_ramki_szare(width: int, height: int, grub: int) -> Image:

    arr_size: (int, int, int) = (height, width, 3)
    CZARNY: (int, int, int) = (0, 0, 0)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości ramki.")

    obraz_arr = np.zeros(arr_size, dtype=np.uint8)

    # Narysuj pierwszą ramkę
    obraz_arr[:grub, :width] = K
    obraz_arr[height - grub:height, :width] = K
    obraz_arr[:height, :grub] = K
    obraz_arr[:height, width - grub:width] = K

    # Narysuj środkowe ramki
    # Przejdź od grub do środka obrazu z krokiem grub
    step = 1
    for i in range(grub, min(width, height) // 2, grub):
        # Ustaw punkty od tak, aby każdy kolejny pasek był o 10% jaśniejszym
        # odcieniem szarości, aż do białego i zapętlaj
        obraz_arr[i:-i, i:-i] = ((25.5 * step) % 255, (25.5 * step) % 255, (25.5 * step) % 255)
        obraz_arr[i + grub:-i - grub, i + grub:-i - grub] = ((25.5 * (step + 1)) % 255, (25.5 * (step + 1)) % 255, (25.5 * (step + 1)) % 255)
        step += 2

    return Image.fromarray(obraz_arr)


def rysuj_pasy_pionowe_cmyk(width: int, height: int, grub: int) -> Image:

    arr_size: (int, int, int) = (height, width, 3)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości pasów.")

    obraz_arr = np.zeros(arr_size, dtype=np.uint8)

    # Przejdź po tablicy z krokiem grub
    step = 0
    for x in range(0, width, grub):
        for y in range(height):
            if step % 4 == 0:
                obraz_arr[y, x:x + grub] = C
            elif step % 4 == 1:
                obraz_arr[y, x:x + grub] = M
            elif step % 4 == 2:
                obraz_arr[y, x:x + grub] = Y
            else:
                obraz_arr[y, x:x + grub] = K
        step += 1

    return Image.fromarray(obraz_arr)


def generuj_ramki_cmyk(width: int, height: int, grub: int) -> Image:

    arr_size: (int, int, int) = (height, width, 3)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości ramki.")

    obraz_arr = np.zeros(arr_size, dtype=np.uint8)

    # Narysuj pierwszą ramkę
    obraz_arr[:grub, :width] = C
    obraz_arr[height - grub:height, :width] = C
    obraz_arr[:height, :grub] = C
    obraz_arr[:height, width - grub:width] = C

    # Narysuj środkowe ramki
    # Przejdź od grub do środka obrazu z krokiem grub
    step = 1
    for i in range(grub, min(width, height) // 2, grub):
        if step % 4 == 0:
            color_1 = C
            color_2 = M
        elif step % 4 == 1:
            color_1 = M
            color_2 = Y
        elif step % 4 == 2:
            color_1 = Y
            color_2 = K
        else:
            color_1 = K
            color_2 = C

        obraz_arr[i:-i, i:-i] = color_1
        obraz_arr[i + grub:-i - grub, i + grub:-i - grub] = color_2
        step += 1

    return Image.fromarray(obraz_arr)


def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg

def negatyw_kolor(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg

# image = rysuj_pasy_pionowe_szare(256, 256, 10)
# image.show()
# image = generuj_ramki_szare(256, 256, 10)
# image.show()
# image = rysuj_pasy_pionowe_cmyk(256, 256, 10)
# image.show()
# image = generuj_ramki_cmyk(256, 256, 10)
# image.show()