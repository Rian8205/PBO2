# Nama    : Rian Saputra
# NIM     : 210511056
# Kelas   : R2/B


class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(c):
        f = (9/5) * c + 32
        return f

    @staticmethod
    def celcius_to_reamur(c):
        r = (4/5) * c
        return r

    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273.15
        return k

# Contoh penggunaan
C = 40
F = Suhu.celcius_to_fahrenheit(C)
R = Suhu.celcius_to_reamur(C)
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "derajat Celcius adalah:", F, "derajat Fahrenheit,", R, "derajat Reamur, dan", K, "derajat Kelvin")