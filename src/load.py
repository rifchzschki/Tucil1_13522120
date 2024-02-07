# Proses Membaca Data Awal dari file .txt maupun dari CLI
import os
# from main import height_matrix

# Initialize resource
buffer_size = 0
width_matrix, height_matrix = 0, 0
matrix = None # matriks[["7A" "55" "E9"], ["E9" "1C" "55"]]
sequence = None # array[[["BD", "E9", "1C"],(15)]]

def load_file(nama_file):
    file_name = nama_file+ ".txt"
    path = os.path.join("test\\load", file_name)
    
    file = open(path, "r")

    # buffer_size = file.readline()

    file.close()

def load_CLI():
    # print(height_matrix)
    global height_matrix
    height_matrix = 10