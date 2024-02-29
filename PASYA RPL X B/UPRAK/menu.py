product = {
    "caffe americano" : 37000, 
    "caramel machiato" : 59000,
    "asian dolce latte" : 55000,
    "caramel latte" : 52000,
    "vanilla latte" : 52000,
    "caffe latte" : 48000,
    "cappuchino" : 48000,
    "caffe mocha" :55000,
}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for coffe, harga in product.items():
        print(f"{coffe}: Rp{harga} per gelas") 

total_belanja = 0
while True:
        coffe_dipilih = input("Masukkan nama coffe yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if coffe_dipilih.lower() == 'selesai':
             break
        if coffe_dipilih not in product:
            print("Maaf, coffe tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa gelas {coffe_dipilih} yang anda inginkan?"))
        total_belanja += product[coffe_dipilih] * jumlah
print(f"total Belanja anda adalah: Rp{total_belanja}")

# Apply PPN tax
ppn = total_belanja *0,1
print(f"PPN 16%: Rp{ppn:.2f}")

# Apply PPN tax
ppn = total_belanja > 350000
diskon = total_belanja * 0,15
print(f"Diskon 15%: Rp{diskon:.2f}")
total_belanja -= diskon

print(f"Total belanja anda setelah pajak dan diskon: Rp{total_belanja:.2f}")

belanja()
