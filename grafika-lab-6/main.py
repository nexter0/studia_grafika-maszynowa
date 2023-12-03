from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjalny.bmp")


def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly(obraz: Image, inicjaly: Image, m: int, n: int, kolor: (int, int, int)) -> Image:
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                obraz1.putpixel((i + m, j + n), kolor)
    return obraz1


def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z) -> Image:
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz1


def wstaw_inicjaly_load(obraz: Image, inicjaly: Image, m: int, n: int, kolor: (int, int, int)) -> Image:
    obraz1 = obraz.copy()
    pixele_obraz = obraz1.load()
    pixele_inicjaly = inicjaly.load()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if pixele_inicjaly[i, j] == 0:
                pixele_obraz[i + m, j + n] = kolor
    return obraz1


def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z) -> Image:
    obraz1 = obraz.copy()
    pixele_obraz = obraz1.load()
    pixele_inicjaly = inicjaly.load()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if pixele_inicjaly[i, j] == 0:
                p = pixele_obraz[i + m, j + m]
                pixele_obraz[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
    return obraz1


def kontrast(obraz, wsp_kontrastu):
    obraz1 = obraz.copy()
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz1.point(lambda i: 128 + (i - 128) * mn)

obraz1 = wstaw_inicjaly_load(obraz, inicjaly, 160, 743, (255, 0, 0))
obraz1.show()

obraz2 = wstaw_inicjaly_maska_load(obraz, inicjaly, 120, 450, 40, -20, -20)
obraz2.show()
obraz1 = wstaw_inicjaly(obraz, inicjaly, 160, 743, (255, 0, 0))
obraz1.show()
obraz1.save("obraz1.png")
obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, 120, 450, 40, -20, -20)
obraz2.show()
obraz2.save("obraz2.png")

obraz_kon1 = kontrast(obraz, 10)
obraz_kon2 = kontrast(obraz, 50)
obraz_kon3 = kontrast(obraz, 100)

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obraz_kon1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obraz_kon2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(obraz_kon3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')


def filtr_liniowy(image, a, b): # a, b liczby całkowite
    image1 = image.copy()
    w, h = image.size
    pixele = image1.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)
    return image1


def transformacja_logarytmiczna(obraz):
    obraz1 = obraz.copy()
    return obraz1.point(lambda i: 255 * np.log(1 + i / 255))


obraz_fl = filtr_liniowy(obraz, 2, 100)
obraz_log = transformacja_logarytmiczna(obraz)

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(obraz_fl)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(obraz_log)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)

obraz_gamma1 = transformacja_gamma(obraz, 10)
obraz_gamma2 = transformacja_gamma(obraz, 50.7)
obraz_gamma3 = transformacja_gamma(obraz, 100)

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(obraz_gamma1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(obraz_gamma2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(obraz_gamma3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
obraz1 = obraz.copy()
T = np.array(obraz1, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, "RGB")
obraz_wynik.show()

# jeżeli nieprawda, że i > wsp wstaw 0 a w przeciwnym przypadku wstaw 255def efekt_plakatu(im, wsp):
obraz1.point(lambda i: i + 200)
obraz1.show()

def rozjasnij(obraz, wsp):
    obraz1 = obraz.copy()
    pixel = obraz1.load()
    w, h = obraz1.size
    for i, j in zakres(w, h):
            r, g, b = pixel[i, j]
            r = r + wsp
            if r > 255:
                r = 255
            g = g + wsp
            if g > 255:
                g = 255
            b = b + wsp
            if b > 255:
                b = 255
            pixel[i, j] = (r, g, b)
    return obraz1


obraz_do_roz = obraz.copy()
obraz_roz = rozjasnij(obraz_do_roz, 100)
obraz_roz.show()
