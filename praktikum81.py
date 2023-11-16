def penjumlahan_rekursif(jumlah, iterasi=1):
    if iterasi > jumlah:
        return 0
    else:
        angka = float(input("Masukkan angka ke-{}: ".format(iterasi)))
        return angka + penjumlahan_rekursif(jumlah, iterasi + 1)

jumlah_angka = int(input("Masukkan Jumlah: "))
hasil = penjumlahan_rekursif(jumlah_angka)
print("Hasil penjumlahan berurut adalah:", hasil)

