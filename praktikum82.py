def perpangkatan(base, power):
    if power == 0:
        return 1
    elif power > 0:
        return base * perpangkatan(base, power - 1)
    else:
        return 1 / (base * perpangkatan(base, -power - 1))

def main():
    while True:
        print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
        angka = input("Masukkan angka: ")
        if angka == "":
            print("Program selesai.")
            break
        pangkat = int(input("Masukkan pangkatnya: "))
        hasil = perpangkatan(float(angka), pangkat)
        print(f"Hasilnya adalah {hasil}")

if __name__ == "__main__":
    main()


