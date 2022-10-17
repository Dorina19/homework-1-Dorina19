from __future__ import annotations
from functools import total_ordering


@total_ordering
class Valuta:
    nev: str
    jel: str
    __arf: float

    def __init__(self, nev: str, jel: str, arf: float) -> None:
        self.nev = nev
        self.jel = jel
        self.__arf = arf

    @property
    def tul(self) -> float:
        return self.__arf

    @tul.setter
    def tul(self, value: float) -> None:
        self.__arf = value

    def __repr__(self) -> str:
        return f"{self.nev}, {self.jel}, {self.__arf}"

    def __str__(self) -> str:
        return f"{self.jel} ({self.nev}): ${self.__arf}"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Valuta):
            return NotImplemented
        return self.nev == o.nev and self.jel == o.jel and self.__arf == o.__arf

    def __lt__(self, other) -> bool:
        if not isinstance(other, Valuta):
            return NotImplemented
        return (-self.__arf, self.nev, self.jel) < (-other.__arf, other.nev, other.jel)

    def __hash__(self) -> int:
        return self.nev.__hash__() + self.jel.__hash__() + self.__arf.__hash__()

    @staticmethod
    def val(lista: list[Valuta], folyam: float) -> list[Valuta]:
        valutak = []
        for i in lista:
            if i.jel > str(folyam):
                valutak.append(i)
        return valutak


class Cval(Valuta):
    __tnev: str

    def __init__(self, nev: str, jel: str, arf: float, tnev: str) -> None:
        super().__init__(nev, jel, arf)
        self.__tnev = tnev

    @property
    def tervezo(self) -> str:
        return self.__tnev

    @tervezo.setter
    def tervezo(self, value: str) -> None:
        self.__tnev = value

    def __repr__(self) -> str:
        return super().__repr__() + f", {self.__tnev}"

    def __str__(self) -> str:
        return super().__str__() + f", @{self.__tnev}"