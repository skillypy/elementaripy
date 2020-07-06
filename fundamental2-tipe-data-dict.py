"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
dict - dicttionary = kamus
"""
kamus_ind_eng = {'anak': 'children', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['ayah'])

print('\nData dari server GoJek, utk mengetahui driver sekitar')
server_gojek = {
    'tgl': '2020-07-06',
    'driver_list': [{'nama': 'eko', 'jarak': 10}, {'nama': 'dwi', 'jarak': 20}, {'nama': 'ari', 'jarak': 30},
                    {'nama': 'ian', 'jarak': 40}]
}
print(server_gojek)
print(f"Driver disekitar sini {server_gojek['driver_list']}")
print(f"Tanggal server gojek sekarang {server_gojek['tgl']}")
print(f"Data driver #3 {server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {server_gojek['driver_list'][3]['jarak']} meter")

