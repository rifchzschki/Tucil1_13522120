# Seluruh Instruksi Utama Program
import sys
from load import load_file, load_CLI
from utils import *

def process(matrix, buffer_size, sequences):
    paths = [] # akan mengandung path dan coordinates
    best_reward = 0; best_path=None; best_coordinate=None
    # Iterasi untuk mencari path yang dimulai dari setiap titik di baris pertama
    for col in range(len(matrix[0])):
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # Reset visited setiap iterasi
        visited[0][col] = True
        find_paths(matrix, paths, buffer_size, 0, col, 1, [matrix[0][col]], [(0, col)], visited)
        visited[0][col] = False

    # Cetak hasil path
    for path, coordinates in paths:
        total_reward, seq_matched = check_sequence_in_path(path, sequences)
        # if(path == ['7A', 'BD', '7A', 'BD', '1C', 'BD', '55']):
        print("Path:", path)
        print(total_reward)
        print("Coordinates:", coordinates)
        print()
        if total_reward>best_reward:
            best_path, best_coordinate, best_reward = path, coordinates, total_reward
    
    return best_path, best_coordinate, best_reward



# preprocess
def load():
    if len(sys.argv)>1:
        arg = sys.argv[1]
        buffer_size, width, height, matrix, num_seq, seqs = load_file(arg)
        # print(seqs)
        buffer, coor, reward = process(matrix, buffer_size, seqs)
        print(buffer, coor, reward)
        # if (len(buffer)!=0):
        #     print (buffer, reward, coor)
        # else:
        #     print("Tidak ada solusi")
    else:
        load_CLI()
        


if __name__ == "__main__": 
    load()