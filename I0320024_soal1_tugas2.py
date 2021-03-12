## menghitung luas persegi panjang

# pengenalan program
print("--- Menghitung luas persegi panjang ---")

# penginputan panjang dan lebar persegi panjang
panjang = float(input("masukkan panjang: " ))
lebar = float(input("masukkan lebar: "))

# proses penghitungan luas
LuasPersegiPanjang = panjang * lebar

# menampilkan hasil
print("Luas Persegi Panjang =", LuasPersegiPanjang, "\n")

## menghitung luas lingkaran

# pengenalan program
print("--- Menghitung luas lingkaran ---")

# penginputan jari-jari lingkaran
r = float(input("masukkan jari-jari: "))

# proses penghitungan luas
luasLingkaran = 3.14 * (r ** 2)

# menampilkan hasil
print("Luas lingkaran =", luasLingkaran, "\n")

## menghitung luas kubus

# pengenalan program
print("--- Menghitung luas kubus ---")

# penginputan rusuk kubus
s = float(input("Masukkan panjang rusuk: "))

# proses penghitungan luas
luaskubus = 6 * (s ** 2)

# menampilkan hasil
print("Luas kubus=", luaskubus, "\n")

## menghitung konversi suhu celcius ke fahrenheit

# pengenalan program
print("--- Konversi suhu celcius ke fahreheit ---")

# penginputan data celcius
celcius = float(input("Masukkan suhu celcius: "))

# proses penghitungan celcius ke fahrenheit
fahrenheit = (celcius * (9/5)) + 32

# menampilkan hasil suhu
print(celcius, "celcius =", fahrenheit, "fahrenheit", "\n")

## menghitung konversi suhu reamur ke kelvin

# pengenalan program
print("--- Konversi suhu reamur ke kelvin ---")

# penginputan data reamur
reamur = float(input("Masukkan suhu reamur: "))

#proses penghitungan celcius ke kelvin
kelvin = (reamur * (5/4)) + 273.15

# menampilkan hasil suhu
print(reamur, "reamur =", kelvin, "kelvin")
