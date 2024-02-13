# Berisi fungsi/prosedur yang dipakai berulang kali untuk keperluan lintas file
def find_sublist(list1, list2):
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
    
    # Mengembalikan sublist terbesar
    return list1[max_index:max_index + max_length]

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
    
    # Menghapus sublist dari list1
    # inter = list1[max_index:max_index + max_length].copy()
    print(find_sublist(list1, list2))
    print("ngetes",(max_index),len(list1))
    if list1[max_index] == list2[0] and list1[max_index + max_length - 1] == list1[-1]:
        # print("asu")
        # del list1[max_index:max_index + max_length]
        del_el_buffer(list1, max_index)
        # return list1[:max_index]
    # else:
        # return list1

def insert_buffer(buffer, seq):
    for token in seq:
        buffer.append(token)

def del_el_buffer(buffer, init):
    i=0
    while(i<len(buffer)):
        if i>= init:
            buffer.pop(i)
            i-=1
        i+=1

def del_inter(buffer, inter):
    if(len(buffer)!=0 and len(inter)!=0):
        i = len(buffer)-1
        while(i>=0):
            if(inter[0]==buffer[i]):
                count = 0
                j = 0
                while j<len(inter):
                    if buffer[i+j] == inter[j]:
                        count+=1
                    j+=1
                if count == len(inter):
                    result = buffer[:i]
                    break
            i-=1
    else:
        result = buffer
    return result

# del_inter(["7A", "BD", "7A", "BD"], ["7A", "BD"])
# print(find_sublist(["7A", "BD", "7A", "BD"], ["7A", "BD","a"]))
# lista = [[1,2,3,4],10]
# lista[0] = lista[0][2:]
# print(lista)

def check_sequence_in_path(path,sequences):
    total_reward = 0  # Inisialisasi total reward
    matched_sequences = []  # Inisialisasi daftar sequence yang cocok

    # Iterasi melalui setiap sequence yang telah didefinisikan
    for seq in sequences:
        sequence = seq[0]
        reward = seq[1]
        # print(reward)
        seq_length = len(sequence)
        path_length = len(path)
        # Iterasi melalui setiap token dalam path
        for i in range(path_length - seq_length + 1):
            # Bandingkan token dalam path dengan token dalam sequence
            if path[i:i+seq_length] == list(sequence):
                # Jika sequence ditemukan dalam path, tambahkan reward dan sequence ke total_reward dan matched_sequences
                total_reward += reward
                matched_sequences.append(sequence)
    # Kembalikan total_reward dan matched_sequences
    return total_reward, matched_sequences

# sequences = [[['BD', 'E9', '1C'], 15],[['BD', '7A', 'BD'], 20],[['BD', '1C', 'BD', '55'], 30]]

# # Contoh path yang akan diperiksa
# example_path = ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55']

# # Memeriksa apakah sequence ada dalam path
# total_reward, matched_sequences = check_sequence_in_path(example_path, sequences)

# # Output hasil
# if matched_sequences:
#     print("Sequence yang ditemukan dalam path:", matched_sequences)
#     print("Total Reward:", total_reward)
# else:
#     print("Tidak ada sequence yang ditemukan dalam path.")

def find_paths(matrix, paths, buffer_size, row, col, path_length, current_path, path_coordinates, visited):
    if path_length == buffer_size:
        paths.append((current_path, path_coordinates))  # Menambahkan path dan koordinatnya ke daftar hasil
        return

    if row > 0 and not visited[row - 1][col]:
        visited[row - 1][col] = True
        find_paths(matrix, paths, buffer_size, row - 1, col, path_length + 1, current_path + [matrix[row - 1][col]], path_coordinates + [(row - 1, col)], visited)
        visited[row - 1][col] = False

    if row < len(matrix) - 1 and not visited[row + 1][col]:
        visited[row + 1][col] = True
        find_paths(matrix, paths, buffer_size, row + 1, col, path_length + 1, current_path + [matrix[row + 1][col]], path_coordinates + [(row + 1, col)], visited)
        visited[row + 1][col] = False

    if col > 0 and not visited[row][col - 1]:
        visited[row][col - 1] = True
        find_paths(matrix, paths, buffer_size, row, col - 1, path_length + 1, current_path + [matrix[row][col - 1]], path_coordinates + [(row, col - 1)], visited)
        visited[row][col - 1] = False

    if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
        visited[row][col + 1] = True
        find_paths(matrix, paths, buffer_size, row, col + 1, path_length + 1, current_path + [matrix[row][col + 1]], path_coordinates + [(row, col + 1)], visited)
        visited[row][col + 1] = False

# # Inisialisasi daftar hasil
# paths = []

# # Matriks yang diberikan
# matrix = [
#     ['7A', '55', 'E9', 'E9', '1C', '55'],
#     ['55', '7A', '1C', '7A', 'E9', '55'],
#     ['55', '1C', '1C', '55', 'E9', 'BD'],
#     ['BD', '1C', '7A', '1C', '55', 'BD'],
#     ['BD', '55', 'BD', '7A', '1C', '1C'],
#     ['1C', '55', '55', '7A', '55', '7A']
# ]

# # Iterasi untuk mencari path yang dimulai dari setiap titik di baris pertama
# for col in range(len(matrix[0])):
#     visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # Reset visited setiap iterasi
#     visited[0][col] = True
#     find_paths(matrix, 0, col, 1, [matrix[0][col]], [(0, col)], visited)
#     visited[0][col] = False

# # Cetak hasil path
# for path, coordinates in paths:
#     print("Path:", path)
#     print("Coordinates:", coordinates)
#     print()


