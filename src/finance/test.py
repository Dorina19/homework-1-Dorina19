import sys

from model import Valuta
from model import Cval


def main():
    assert len(sys.argv) > 1
    n = int(sys.argv[1])
    assert n > 0
    val = []

    for i in range(n):
        ertek = input()
        darabol = ertek.split(";")
        if len(darabol) == 3:
            x = Valuta(darabol[0], darabol[1], float(darabol[2]))
            val.append(x)
        elif len(darabol) == 4:
            y = Cval(darabol[0], darabol[1], float(darabol[2]), darabol[3])
            val.append(y)
        else:
            print("Hibás a bemenet!")

        val.sort()
        for v in val:
            print(v)

if __name__ == '__main__':
    main() 