alo_f = open("aloha.txt")
haw_f = open("hawai.txt")
print('Contenido de los archivos: \n')
[print(i, end=' ') for f in [haw_f, alo_f] for i in f]