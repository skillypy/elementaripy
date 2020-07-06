print('tipe data skalar = sederhana')
anak1 = 'Awal'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Tunggal'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Awal','Dwi','Tri','Tunggal']
print(anak)
print('tambah anak(list) pake append')
anak.append('Akhir')
print(anak)

print('\nsapa anak ke-2 (index hitungan di mulai dari 0)')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak (for in)')
for a in anak:
    print(f'Hai {a}!')

print('\nsapa anak cara ribet (for in range + len)')
for a in range (0, len(anak)):
    print(f'{a+1}.Hai {anak[a]}')