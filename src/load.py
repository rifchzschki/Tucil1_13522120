# Proses Membaca Data Awal dari file .txt maupun dari CLI
import os
from random import randint
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
    n_token = int(input("Jumlah token: "))
    token = []
    for i in range(n_token):
        tok = input()
        token.append(tok)
    buffer_size =  int(input("Ukuran buffer: "))
    h_matrix = int(input("Tinggi matriks: "))
    w_matrix = int(input("Lebar matriks: "))
    num_seq = int(input("Jumlah sekuens: "))
    size_max_seq = int(input("Ukuran maks sekuens: "))

    # buat matriks
    matrix = [[token[randint(0,len(token)-1)]for i in range (w_matrix)] for j in range(h_matrix)]
    sequens = []
    for i in range(num_seq):
        seq = [token[randint(0,len(token)-1)] for i in range(randint(1,size_max_seq))]
        reward = randint(0,50)
        sequens.append([seq,reward])
    # print(matrix, sequens)
    return matrix, sequens, h_matrix, w_matrix, buffer_size, num_seq
# load_CLI()