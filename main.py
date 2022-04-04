import ezdxf
import math

print("Podaj nazwe pliku dxf")
nazwa_pliku = input(str())
nazwa_pliku = nazwa_pliku + ".dxf"

file = ezdxf.readfile(nazwa_pliku)
msp = file.modelspace()
longitud_total = 0
number_of_line = 0


def print_entity(e):
    if e.dxftype() == "LINE":
        print("LINE on layer: %s " % e.dxf.layer)
        print("start point: %s " % e.dxf.start)
        print("end point: %s \n" % e.dxf.end)

for block in file.blocks:
    # iterate over all entities in modelspace
    try:
        for e in block:
            print_entity(e)
            dl = math.sqrt((e.dxf.start[0] - e.dxf.end[0]) ** 2 + (e.dxf.start[1] - e.dxf.end[1]) ** 2)
            print("linea: " + str(dl))
            longitud_total = longitud_total + dl
            print("Longitud Total: " + str(longitud_total) + "\n")
    except:
        continue


