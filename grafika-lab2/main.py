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
                obraz_arr[(row_number - 1) - row][(col_number - 1) - col] = 0
        else:
            for col in range(0, grub):
                obraz_arr[row][col] = 0
                obraz_arr[row][(col_number - 1) - col] = 0

    obraz_arr = obraz_arr.astype(bool)
    obraz = Image.fromarray(obraz_arr)

    return obraz


def generuj_ramki(width: int, height: int, grub: int):
    obraz_arr = np.ones((width, height))

    row_number: int = len(obraz_arr)
    col_number: int = len(obraz_arr[0])
    while (cols / 2)
    for row in range(0, row_number):
        if row <= grub - 1:
            for col in range(0, col_number):
                obraz_arr[row][col] = 0
                obraz_arr[(row_number - 1) - row][(col_number - 1) - col] = 0
        else:
            for col in range(0, grub):
                obraz_arr[row][col] = 0
                obraz_arr[row][(col_number - 1) - col] = 0
    step += 2 * grub
    obraz_arr = obraz_arr.astype(bool)
    obraz = Image.fromarray(obraz_arr)

    obraz.show()


def zad2() -> None:
    image = Image.open("inicjaly.bmp")

    ramka5 = rysuj_ramke(image, 5)
    ramka10 = rysuj_ramke(image, 10)
    ramka5.save("ramka5.bmp")
    ramka10.save("ramka10.bmp")

# exec
# zad2()
generuj_ramki(50, 50, 10)

