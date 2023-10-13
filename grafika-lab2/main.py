import numpy as np
from PIL import Image

def rysuj_ramke_w_obrazie(obraz: Image, grub: int) -> None:
    obraz_arr = np.asarray(obraz) * 1
    obraz_arr_row_count = len(obraz_arr)
    obraz_arr_col_count = len(obraz_arr[0])
    for row in range(0, obraz_arr_row_count):
        for col in range(0, obraz_arr_col_count)
            if row <= grub:
                obraz_arr[row][col] =
    obraz.show()

image = Image.open("inicjaly.bmp")

rysuj_ramke_w_obrazie(image, 3)


