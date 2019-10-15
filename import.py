import pemuaian

def main():

    #Menghitung Pemuaian Panjang
    p = 54
    k = 20
    t = 25
    
    #Rumus Pemuaian Panjang
    muaiPanjang = pemuaian.pemuaianPanjang(p, k, t)

    print("Rumus Pemuaian Panjang")
    print("Panjang\t\t: ", p)
    print("Koefisien\t: ", k)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", muaiPanjang)

    #Menghitung Pemuaian Luas
    l = 31
    L = 34
    t = 12

    #Rumus Pemuaian Luas
    muaiLuas = pemuaian.pemuaianLuas(l, L, t)

    print("\nRumus Pemuaian Luas")
    print("Luas\t\t: ", l)
    print("Koefisien\t: ", L)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", muaiLuas)

    #Menghitung Pemuaian Volume
    v = 12
    V = 30
    t = 5

    #Rumus Pemuaian Volume
    muaiVolume = pemuaian.pemuaianVolume(v, V, t)

    print("\nRumus Pemuaian Volume")
    print("Volume\t\t: ", v)
    print("Koefisien\t: ", V)
    print("Waktu\t\t: ", t)
    print("Hasil\t\t: ", muaiVolume)

if __name__ == "__main__":
    main()
