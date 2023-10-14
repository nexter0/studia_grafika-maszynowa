import numpy as np
from PIL import Image
from typing import List


def rysuj_ramke(obraz: Image, grub: int) -> Image:
    obraz_arr: List[List[int]] = np.asarray(obraz) * 1
    row_number: int = len(obraz_arr)
    col_number: int = len(obraz_arr[0])

    for row in range(0, row_number):
        if row <= grub - 1:
            for col in range(0, col_number):
                obraz_arr[row][col] = 0
                obraz_arr[(row_number - 1) - row][col] = 0
        else:
            for col in range(0, grub):
                obraz_arr[row][col] = 0
                obraz_arr[row][(col_number - 1) - col] = 0

    obraz_arr = obraz_arr.astype(bool)
    obraz = Image.fromarray(obraz_arr)

    return obraz


def generuj_ramki(width: int, height: int, grub: int) -> Image:
    arr_size: (int, int) = (height, width)

    obraz_arr = np.ones(arr_size)

    row_number: int = len(obraz_arr)
    col_number: int = len(obraz_arr[0])

    step = 0

    while step < col_number / 2:

        for row in range(step, row_number - step):
            if row <= grub + step - 1:
                for col in range(step, col_number - step):
                    obraz_arr[row][col] = 0
                    obraz_arr[(row_number - 1) - row][col] = 0
            else:
                for col in range(step, grub + step):
                    obraz_arr[row][col] = 0
                    obraz_arr[row][(col_number - 1) - col] = 0

        step += 2 * grub

    obraz_arr = obraz_arr.astype(bool)

    return Image.fromarray(obraz_arr)


def rysuj_pasy_pionowe(width, height, grub) -> Image:
    arr_size: (int, int) = (height, width)

    obraz_arr = np.ones(arr_size)

    bars_number = int(width / grub)
    for bar in range(bars_number):
        for g in range(grub):
            i = bar * grub + g
            for j in range(height):
                obraz_arr[j, i] = bar % 2

    obraz_arr = obraz_arr * 255

    return Image.fromarray(obraz_arr)


def prostokaty(width, height, m, n) -> Image:
    arr_size: (int, int) = (height, width)

    obraz_arr = np.ones(arr_size)

    row_number: int = len(obraz_arr)
    col_number: int = len(obraz_arr[0])

    for row in range(0, n + 1):
        for col in range(0, m + 1):
            obraz_arr[row, col] = 0

    for row in range(n + 1, row_number):
        for col in range(m + 1, col_number):
            obraz_arr[row, col] = 0


    obraz_arr = obraz_arr.astype(bool)
    img = Image.fromarray(obraz_arr)
    img.show()

# Wywołanie zadań


def zad2() -> None:
    image = Image.open("inicjaly.bmp")

    ramka5 = rysuj_ramke(image, 5)
    ramka10 = rysuj_ramke(image, 10)
    ramka5.save("ramka5.bmp")
    ramka10.save("ramka10.bmp")


def zad3_1() -> None:
    image = generuj_ramki(200, 350, 10)
    image.show()


def zad3_2() -> None:
    image = rysuj_pasy_pionowe(250, 350, 50)
    image.show()


# exec
# zad2()
# zad3_1()
# zad3_2()
prostokaty(100, 200, 30, 50)