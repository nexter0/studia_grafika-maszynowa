from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im: Image) -> None:
    s = stat.Stat(im)
    print("extrema ", s.extrema)
    print("count ", s.count)
    print("mean ", s.mean)
    print("median ", s.median)
    print("stddev ", s.stddev)


def rysuj_histogram_RGB(im: Image) -> None:
    histogram = im.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")
    plt.show()


im = Image.open('diff.png')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
h, w = im.size

statystyki(im)

hist = im.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2*256 + p])

rysuj_histogram_RGB(im)


def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent


def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent


print(zlicz_roznice_srednia_RGB(im, 0))
print(zlicz_roznice_srednia_RGB(im, 10))

print(zlicz_roznice_suma_RGB(im, 0))
print(zlicz_roznice_suma_RGB(im, 10))
print(zlicz_roznice_suma_RGB(im, 30))

im0 = Image.open("obraz.jpg")
im0.save("obraz1.jpg")
im1 = Image.open("obraz1.jpg")
im1.save("obraz2.jpg")
im2 = Image.open("obraz2.jpg")
im2.save("obraz3.jpg")
im3 = Image.open("obraz3.jpg")
im3.save("obraz4.jpg")
im4 = Image.open("obraz4.jpg")
im4.save("obraz5.jpg")
im5 = Image.open("obraz4.jpg")

diff_0_5 = ImageChops.difference(im0, im5)
diff_0_4 = ImageChops.difference(im0, im4)
diff_0_3 = ImageChops.difference(im0, im3)
diff_0_2 = ImageChops.difference(im0, im2)
diff_0_1 = ImageChops.difference(im0, im1)
diff_4_5 = ImageChops.difference(im4, im5)
print("roznica 0 vs 1", zlicz_roznice_srednia_RGB(diff_0_1, 0))
print("roznica 0 vs 2", zlicz_roznice_srednia_RGB(diff_0_2, 0))
print("roznica 0 vs 3", zlicz_roznice_srednia_RGB(diff_0_3, 0))
print("roznica 0 vs 4", zlicz_roznice_srednia_RGB(diff_0_4, 0))
print("roznica 0 vs 5", zlicz_roznice_srednia_RGB(diff_0_5, 0))
print("roznica 4 vs 5", zlicz_roznice_srednia_RGB(diff_4_5, 0))


def odkoduj(obraz1: Image, obraz2: Image) -> Image:
    ob1arr = np.asarray(obraz1)
    ob2arr = np.asarray(obraz2)
    h, w = obraz1.size
    h2, w2 = obraz2.size
    if h != h2 or w != w2:
        raise Exception("Niewłaściwy rozmiar obrazu.")
    diff = ImageChops.difference(obraz1, obraz2)
    diffarr = np.asarray(diff)
    code = [[0 if np.array_equal(element, [0, 0, 0]) else 1 for element in row] for row in diffarr]
    codeimg = Image.fromarray(np.array(code, dtype=np.uint8) * 255)
    return codeimg


jesen = Image.open("jesien.jpg")
kod = Image.open("zakodowany2.bmp")

odkodowany = odkoduj(jesen, kod)
odkodowany.show()
odkodowany.save("kod2.bmp")
