# Proses Membaca Data Awal dari file .txt maupun dari CLI
import os
# from main import height_matrix

# Initialize resource
# buffer_size = 0
# width_matrix, height_matrix = 0, 0
# matrix = None # matriks[["7A" "55" "E9"], ["E9" "1C" "55"]]
# sequence = None # array[[["BD", "E9", "1C"],(15)]]

def load_file(nama_file):
    file_name = nama_file+ ".txt"
    path = os.path.join("test\\load", file_name)
    
    file = open(path, "r")

    buffer_size = int(file.readline())
    width_matrix, height_matrix = file.readline().split()
    width, height = int(width_matrix), int(height_matrix)
    matrix = ["" for i in range(height)]
    for j in range(height):
        matrix[j] = file.readline().split()

    num_seq = int(file.readline())
    seqs = []
    for _ in range(num_seq):
        seq = file.readline().split()
        reward = int(file.readline())
        seqs.append([seq,reward])

    file.close()
    
    return buffer_size, width, height, matrix, num_seq, seqs

def load_CLI():
    ...