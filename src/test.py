# lists = [['BD', 'E9', '1C'], ['BD', '7A', 'BD', 'BD'], ['BD', '1C', 'BD', '55']]

# # Menentukan panjang maksimum dari sublist
# max_length = max(len(sublist) for sublist in lists)

# # Melakukan iterasi pada indeks dari 0 sampai 3
# for i in range(max_length):
#     # Membuat list sementara untuk menyimpan elemen di indeks tertentu dari setiap sublist
#     temp_list = []
#     # Menambahkan elemen dari setiap sublist di indeks i ke dalam list sementara
#     for sublist in lists:
#         if i < len(sublist):  # Memeriksa apakah indeks i ada di dalam sublist
#             temp_list.append(sublist[i])
#         else:
#             temp_list.append(0)

#     # Menampilkan elemen dari list sementara
#     print(temp_list)

# def find_sublist(list1, list2):
#     # Inisialisasi variabel untuk menyimpan panjang sublist terbesar dan indeksnya
#     max_length = 0
#     max_index = -1
    
#     # Iterasi melalui list1 untuk mencari kemunculan sublist
#     for i in range(len(list1)):
#         length = 0
#         j = 0
#         while i + j < len(list1) and j < len(list2) and list1[i + j] == list2[j]:
#             length += 1
#             j += 1
        
#         # Memeriksa apakah sublist ini lebih besar dari yang sebelumnya
#         if length > max_length:
#             max_length = length
#             max_index = i
    
#     # Mengembalikan sublist terbesar
#     return list1[max_index:max_index + max_length]

# # Contoh penggunaan
# list1 = ["BD", "7A", "BD"]
# list2 = ["7A", "BD", "1C", "BD", "55"]

# sublist = find_sublist(list1, list2)
# print("Sublist berurutan terbesar:", sublist)

# def find_and_remove_sublist(list1, list2):
#     # Inisialisasi variabel untuk menyimpan panjang sublist terbesar dan indeksnya
#     max_length = 0
#     max_index = -1
    
#     # Iterasi melalui list1 untuk mencari kemunculan sublist
#     for i in range(len(list1)):
#         length = 0
#         j = 0
#         while i + j < len(list1) and j < len(list2) and list1[i + j] == list2[j]:
#             length += 1
#             j += 1
        
#         # Memeriksa apakah sublist ini lebih besar dari yang sebelumnya
#         if length > max_length:
#             max_length = length
#             max_index = i
    
#     # Menghapus sublist dari list1
#     del list1[max_index:max_index + max_length]

# # Contoh penggunaan
# list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b']
# list2 = ['e', 'f', 'a', 'b', 'g', 'h', 'i']

# find_and_remove_sublist(list1, list2)
# print("list1 setelah menghapus sublist:", list1)

def find_and_remove_sublist(list1, list2):
    # Inisialisasi variabel untuk menyimpan panjang sublist terbesar dan indeksnya
    max_length = 0
    max_index = -1
    
    # Iterasi melalui list1 untuk mencari kemunculan sublist
    for i in range(len(list1)):
        length = 0
        j = 0
        while i + j < len(list1) and j < len(list2) and list1[i + j] == list2[j]:
            length += 1
            j += 1
        
        # Memeriksa apakah sublist ini lebih besar dari yang sebelumnya
        if length > max_length:
            max_length = length
            max_index = i
    
    # Menentukan apakah sublist harus dihapus berdasarkan pengecualian yang ditetapkan
    if list1[max_index] == list2[0] and list1[max_index + max_length - 1] == list1[-1]:
        # Menghapus sublist dari list1
        del list1[max_index:max_index + max_length]
        print("Sublist dihapus dari list1.")
    else:
        print("Pengecualian: Sublist tidak dihapus karena tidak sesuai kriteria.")

# Contoh penggunaan
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b']
list2 = ['e', 'f', 'a', 'b', 'g', 'h', 'i']

find_and_remove_sublist(list1, list2)
print("list1 setelah penghapusan sublist:", list1)
