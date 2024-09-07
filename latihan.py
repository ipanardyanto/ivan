nama = "ivan ardyanto";
nim = 240441100088
ipk = 4.00
mahasiswa = True

print("nama saya adalah", nama)
#ini dalah format natural (tipe data sama)
print("nim saya adalah", nim)
print("impian ipk saya adalah", ipk)
print("nama merupakan mahasiswa", mahasiswa)


#ini adalah format string (tipe data diubah mnjadi string)
print(f"nim saya adalah (nim)")


#progam dimanis str
nama_panjang = str(input("nama saya adalah ;"))



#progam dinamis int
nilai_matematika = int(input("nilai saya adalah ;"))

nilai_matematika = 90
nilai_biologi = 75
nilai_kimia = 85
nilai_fisika = 95

penjumlahan = nilai_matematika + nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f'hasil penjumlahan dari matematika adalah ; {penjumlahan}')
print(f'hasil perkalian dari matematika adalah ; {perkalian}')
print(f'hasil perkalian dari matematika adalah ; {pengurangan}')
print(f'hasil perkalian dari matematika adalah ; {pembagian}')


usia_masuk_kuliah = int(input("berapa usia anda ?"))
lama_kuliah = int(input("berapa lama kuliah anda ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'saaat ini, saya (nama) berumur{usia_saat_ini}')
print(f'saya (nama) akan lulus pada tahun{tahun_lulus}')

