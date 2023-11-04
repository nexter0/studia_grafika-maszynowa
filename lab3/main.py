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


def gradient_red(image: Image) -> Image:
    arr_origin = np.asarray(image)
    print(arr_origin.shape)
    h, w = arr_origin.shape
    new_arr_size = (h, w, 3)
    arr = np.ones(new_arr_size, dtype=np.uint8)
    step_size = 255 // h  # Im mniejszy obraz tym szybciej zmieniaj kolor (aby cały obraz nie był czarny)
    if step_size == 0:
        step_size = 1
    step = 0
    color_switch = 0
    for i in range(h):
        for j in range(w):
            if arr_origin[i, j] == False:
                if color_switch % 3 == 0:
                    arr[i, j] = [step, 0, 0]
                elif color_switch % 3 == 1:
                    arr[i, j] = [255, step, 0]
                elif color_switch % 3 == 2:
                    arr[i, j] = [255, 255, step]
            else:
                arr[i, j] = [255, 255, 255]
        step += step_size
        if step >= 255:
            step = 0
            color_switch += 1

    return Image.fromarray(arr)


def negatyw(image: Image) -> Image:
    arr = np.asarray(image)
    h, w, rgb = arr.shape
    arr_neg = arr.copy()
    for i in range(h):
        for j in range(w):
            for k in range(rgb):
                arr_neg[i, j, k] = 255 - arr[i, j, k]
    return Image.fromarray(arr_neg)


def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return tab


# image5 = Image.open("inicjaly.bmp")
# image5_kolor = Image.fromarray(koloruj_obraz(image5, [-24, 0, 0]))
# image5.show()

image1 = rysuj_pasy_pionowe_szare(255, 255, 5)
print(image1.mode)
# image1_N = negatyw(image1)
# image2 = generuj_ramki_szare(255, 255, 5)
# image2_N = negatyw(image2)
# image3 = rysuj_pasy_pionowe_cmyk(255, 255, 5)
# image3_N = negatyw(image3)
# image4 = gradient_red(Image.open("inicjaly.bmp"))
# image6 = generuj_ramki_cmyk(255, 255, 5)
# image6_N = negatyw(image6)

# image1.save("obraz1_1.jpg")
# image1_N.save("obraz1_1N.jpg")
# image1.save("obraz1_1.png")
# image1_N.save("obraz1_1N.png")
# image2.save("obraz1_2.jpg")
# image2_N.save("obraz1_2N.jpg")
# image2.save("obraz1_2.png")
# image2_N.save("obraz1_2N.png")
# image3.save("obraz2_1.jpg")
# image3_N.save("obraz2_1N.jpg")
# image3.save("obraz2_1.png")
# image3_N.save("obraz2_1N.png")


# image6.save("obraz2_2.jpg")
# image6_N.save("obraz2_2N.jpg")
# image6.save("obraz2_2.png")
# image6_N.save("obraz2_2N.png")

