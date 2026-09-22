#Membuat function untuk menghitung biaya pemesanan hotel
def hitung_biaya_hotel(jenis_kamar, durasi_malam):
    if jenis_kamar.lower() == "standard":
        tarif_per_malam = 200000
    elif jenis_kamar.lower() == "deluxe":
        tarif_per_malam = 350000
    else:
        tarif_per_malam = 0
        
    total_biaya = tarif_per_malam * durasi_malam
    return total_biaya

#tanggal check-in dan check-out
tanggal_checkin = 1
tanggal_checkout = 5
jenis_kamar_dipesan = "Deluxe"

#menentukan lama menginap dari selisih tanggal check-out dikurang check-in
lama_inap = tanggal_checkout - tanggal_checkin

#panggil function dengan data jenis kamar dan lama menginap
total_harga = hitung_biaya_hotel(jenis_kamar_dipesan, lama_inap)

#7. Menampilkan hasil
print("Jenis Kamar      :", jenis_kamar_dipesan)
print("Tanggal Check-in :", tanggal_checkin, "Oktober 2026")
print("Tanggal Check-out:", tanggal_checkout, "Oktober 2026")
print("Lama Menginap    :", lama_inap, "malam")
print("Total Biaya      : Rp", total_harga)