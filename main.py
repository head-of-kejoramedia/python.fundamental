"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu memberi perintah,"Pergi ke toko"')
print('Anak menjawab,"Baik, apa yang harus saya beli di toko?"')
print('Ibu menjawab,"Beli 1 botol susu, kalau ada telur beli 6 butir"')
print('Anak berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_butir_telur = 153
print(f'Jumlah botol susu {jumlah_botol_susu} btl')
print(f'Jumlah butir telur {jumlah_butir_telur} butir')

if jumlah_botol_susu > 0:
    print('Anak membeli 1 botol susu')
else:
    print('Anak tdak membeli susu')

if jumlah_butir_telur >=6:
    print('Anak membeli 6 butir telur')
else:
    print('Anak tidak membeli telur')

print('Anak pulang ke rumah')
print('Anak laporan hasil belanja ke Ibu')
