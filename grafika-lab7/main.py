from PIL import Image
import numpy as np


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            if pixel[0] > temp[0]:
                temp[0] = pixel[0]
            if pixel[1] > temp[1]:
                temp[1] = pixel[1]
            if pixel[2] > temp[2]:
                temp[2] = pixel[2]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1


def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            if pixel[0] < temp[0]:
                temp[0] = pixel[0]
            if pixel[1] < temp[1]:
                temp[1] = pixel[1]
            if pixel[2] < temp[2]:
                temp[2] = pixel[2]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1


def rysuj_kolo(obraz, r, m_s, n_s, x, y):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2:
            pixel = obraz1.getpixel((i, j))
            dx = x - m_s
            dy = y - n_s
            if 0 < i + dx < w and 0 < j + dy < h:
                obraz1.putpixel((i + dx, j + dy), pixel)
    return obraz1

def odbij_w_pionie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1- i, j]
    return img

def odbij_w_pionie3(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img


image = Image.open("IMG20231017121105.jpg")
odbij_w_pionie(image).show()
odbij_w_pionie3(image).show()
image1 = rysuj_kwadrat_max(image, 100, 100, 100)
image1 = rysuj_kwadrat_max(image1, 500, 300, 70)
image1 = rysuj_kwadrat_max(image1, 300, 600, 160)
image1.show()
image1.save("obraz1.png")

image2 = rysuj_kwadrat_min(image, 100, 100, 105)
image2 = rysuj_kwadrat_min(image2, 500, 300, 75)
image2 = rysuj_kwadrat_min(image2, 300, 600, 165)
image2.show()
image2.save("obraz2.png")

image3 = rysuj_kolo(image, 50, 271, 484, 550, 100)
image3 = rysuj_kolo(image3, 50, 271, 484, 600, 800)
image3 = rysuj_kolo(image3, 120, 271, 484, 100, 0)
image3.show()
image3.save("obraz3.png")
