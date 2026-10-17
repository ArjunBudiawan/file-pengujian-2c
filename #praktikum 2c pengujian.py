#praktikum 2c pengujian
#vscode

def hitung_rata_rata_nilai(nilai1, nilai2, nilai3):
    return (nilai1 + nilai2 + nilai3) / 3

n1= float(input("Masukkan nilai 1: "))
n2= float(input("Masukkan nilai 2: "))
n3= float(input("Masukkan nilai 3: "))

hasil = hitung_rata_rata_nilai(n1, n2, n3)
print(f"Rata-rata dari ketiga nilai adalah: {hasil:.2f}")
