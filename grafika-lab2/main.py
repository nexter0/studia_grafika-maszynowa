import numpy as np
from PIL import Image
from typing import List


def rysuj_ramke(obraz: Image, grub: int) -> Image:
    obraz_arr = np.asarray(obraz) * 1

    rows_number, cols_number = obraz_arr.shape

    if grub <= 0 or grub >= cols_number:
        raise ValueError("Niepoprawna wartość grubości ramki.")

    # Ustaw punkty od (0, 0) do (cols_number, grub) na czarne - ramka górna
    obraz_arr[:grub, :cols_number] = 0

    # Ustaw punkty od (0, row_number - grub) do (cols_number, rows_number) na czarne - ramka dolna
    obraz_arr[rows_number - grub:rows_number, :cols_number] = 0

    # Ustaw punkty od (0,0) do (grub, rows_number) na czarne - ramka lewa
    obraz_arr[:rows_number, :grub] = 0

    # Ustaw punkty od (cols_number, 0) do (cols_number, rows_number) na czarne - ramka prawa
    obraz_arr[:rows_number, cols_number - grub:cols_number] = 0

    obraz_arr = obraz_arr.astype(bool)
    obraz = Image.fromarray(obraz_arr)

    return obraz


def generuj_ramki(width: int, height: int, grub: int) -> Image:
    arr_size: (int, int) = (height, width)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości ramki.")

    obraz_arr = np.ones(arr_size)

    # Narysuj pierwszą ramkę
    obraz_arr[:grub, :width] = 0
    obraz_arr[height - grub:height, :width] = 0
    obraz_arr[:height, :grub] = 0
    obraz_arr[:height, width - grub:width] = 0

    # Narysuj środkowe ramki
    # Przejdź od grub do środka obrazu z krokiem 2 * grub
    for i in range(grub, min(width, height) // 2, 2 * grub):
        # Narysuj biały prostokąt od (i, i) do (width - i, height - i)
        obraz_arr[i:-i, i:-i] = 1
        # Narysuj czarny prostokąt od (i + grub, i + grub) do (width - i - grub, height - i - grub)
        obraz_arr[i + grub:-i - grub, i + grub:-i - grub] = 0

    obraz_arr = obraz_arr.astype(bool)
    return Image.fromarray(obraz_arr)


def rysuj_pasy_pionowe(width: int, height: int, grub: int) -> Image:

    arr_size: (int, int) = (height, width)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if grub <= 0 or grub >= width:
        raise ValueError("Niepoprawna wartość grubości pasów.")

    obraz_arr = np.ones(arr_size)

    # Przejdź po tablicy z krokiem 2 * grub
    for x in range(0, width, 2 * grub):
        for y in range(height):
            # Ustaw punkty od (x, y) do (x + grub, y) na czarne
            obraz_arr[y, x:x + grub] = 0

    obraz_arr = obraz_arr.astype(bool)
    return Image.fromarray(obraz_arr)


def prostokaty(width: int, height: int, m: int, n: int) -> Image:
    arr_size: (int, int) = (height, width)

    if width <= 0 or height <= 0:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if m <= 0 or n <= 0 or m >= width or n >= height:
        raise ValueError("Niepoprawne współrzędne punktu.")

    obraz_arr = np.ones(arr_size)

    # Ustaw punkty (0,0) ... (m, n) na czarne
    obraz_arr[:n, :m] = 0

    # Ustaw punkty (m,n) ... (width, height) na czarne
    obraz_arr[n:, m:] = 0

    obraz_arr = obraz_arr.astype(bool)
    return Image.fromarray(obraz_arr)


def szachownica(size: int, cell_size: int) -> Image:
    arr_size: (int, int) = (size, size)

    if size <= 0 or cell_size <= 0 or cell_size > size // 2:
        raise ValueError("Niepoprawne wymiary obrazka.")
    if size < 2 * cell_size:
        raise ValueError("Niepoprawne rozmiar komórki (komórka nie może być większa niż 50% krawędzi obrazka).")

    obraz_arr = np.ones(arr_size)

    # Przejdź po tablicy z krokiem cell_size
    for i in range(0, size, cell_size):
        for j in range(0, size, cell_size):
            if (i // cell_size + j // cell_size) % 2 == 1:
                # Ustaw punkty (i, j) ... (i + cell_size, j + cell_size) na czarne
                obraz_arr[i:i + cell_size, j:j + cell_size] = 0

    obraz_arr = obraz_arr.astype(bool)
    return Image.fromarray(obraz_arr)


def wstaw_obraz_w_obraz(obraz_bazowy: Image, obraz_wstawiany: Image, m: int, n: int) -> Image:
    tab_obraz = np.asarray(obraz_wstawiany)*1
    h0, w0 = tab_obraz.shape

    tab = np.asarray(obraz_bazowy)*1
    h1, w1 = tab.shape

    n_k = min(h1, n + h0)
    m_k = min(w1, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    print(n_k, m_k)
    print(n_p, m_p)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz[i - n][j - m]
    tab = tab.astype(bool)
    return Image.fromarray(tab)

# Wywołanie zadań


def zad2() -> None:
    image = Image.open("inicjaly.bmp")

    ramka5 = rysuj_ramke(image, 5)
    ramka10 = rysuj_ramke(image, 10)
    ramka5.save("ramka5.bmp")
    ramka10.save("ramka10.bmp")


def zad3_1() -> None:
    image = generuj_ramki(250, 400, 5)
    image.show()


def zad3_2() -> None:
    image = rysuj_pasy_pionowe(269, 350, 20)
    image.show()


def zad3_3() -> None:
    image = prostokaty(250, 350, 20, 300)
    image.show()


def zad3_4() -> None:
    image = szachownica(200, 50)
    image.show()


def zad_4() -> None:
    obraz1 = generuj_ramki(480, 320, 10)
    obraz1.save("obraz1.bmp")
    obraz2 = rysuj_pasy_pionowe(480, 320, 10)
    obraz2.save("obraz2.bmp")
    obraz3 = prostokaty(480, 320, 100, 50)
    obraz3.save("obraz3.bmp")
    obraz4 = szachownica(480, 10)
    obraz4.save("obraz4.bmp")


def zad_5() -> None:
    obraz4 = szachownica(480, 10)
    inicajly = Image.open("inicjaly.bmp")
    wstaw1 = wstaw_obraz_w_obraz(obraz4, inicajly, 300, 90)
    wstaw2 = wstaw_obraz_w_obraz(obraz4, inicajly, 10, 290)
    wstaw1.save("wstaw1.bmp")
    wstaw2.save("wstaw2.bmp")


# exec
# zad2()
# zad3_1()
# zad3_2()
# zad3_4()
# zad_4()
zad_5()