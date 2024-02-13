# Seluruh Instruksi Utama Program
import sys
import time
import os
from load import load_file, load_CLI


# process
def process(matrix, h_matrix, w_matrix, pos, temp_buffer, buffer_size, seq, temp_path, x, y, direction):
    global rew, buffer, path
    
    if len(temp_buffer) > buffer_size:
        return
    
    current_reward = 0
    for i in range(len(seq)):
        for j in range(len(temp_buffer) - len(seq[i][0]) + 1):
            temp_seq = temp_buffer[j:j+len(seq[i][0])]
            if temp_seq == seq[i][0]:
                current_reward += seq[i][1]
    
    if current_reward > rew:
        rew = current_reward
        buffer = temp_buffer.copy()
        path = temp_path.copy()
    
    token = matrix[y][x]
    if direction == 0: # vertical
        for i in range(h_matrix):
            temp_buffer.append(token)
            temp_path.append((x+1, y+1))
            pos[y][x] = 1
            if pos[i][x] == 0:
                process(matrix, h_matrix, w_matrix, pos,temp_buffer, buffer_size, seq, temp_path, x, i, 1)
            pos[y][x] = 0
            temp_buffer.pop()
            temp_path.pop()
    else: # Horizontal
        for i in range(w_matrix):
            temp_buffer.append(token)
            temp_path.append((x+1, y+1))
            pos[y][x] = 1
            if pos[y][i] == 0:
                process(matrix, h_matrix, w_matrix, pos,temp_buffer, buffer_size, seq, temp_path, i, y, 0)
            pos[y][x] = 0
            temp_buffer.pop()
            temp_path.pop()

def start(buffer_size, width, height, matrix, seqs):
    global rew, buffer, path
    pos = [[0] * width for _ in range(height)]
    buffer = []
    path = []
    best_buff = []
    best_path = []
    best_reward = 0
    start_time = time.time()
    for i in range(width):
            rew = 0
            buffer = []
            path = []
            process(matrix, height, width, pos, buffer, buffer_size, seqs, path, i, 0, 0)
            if rew > best_reward:
                best_reward = rew
                best_buff = buffer
                best_path = path
                
    end_time = time.time()
    return best_buff, best_path, best_reward, (end_time-start_time)

# preprocess
def load():
    if len(sys.argv)>1:
        arg = sys.argv[1]
        buffer_size, width, height, matrix, num_seq, seqs = load_file(arg)
        buffer, coor, reward, time = start(buffer_size, width, height, matrix, seqs)
        if (len(buffer)!=0):
            print(reward)
            for i in range(len(buffer)):
                print(buffer[i], end=' ')
            print()
            for j in coor:
                print(j)
            print(f"\n{int(time*1000)} ms")

            simpan = input("Apakah ingin menyimpan solusi? (y/n)")
            if simpan == "y":
                nama = input("Masukkan nama file: ")
                file_path = os.path.join("test\\save", nama)
                with open(file_path,"w") as file:
                    file.write(f"{reward}\n")
                    # file.write(reward)
                    for i in range(len(buffer)):
                        file.write(f"{buffer[i]} ")
                    file.write("\n")
                    for j in coor:
                        file.write(f"{j}\n")
                    file.write(f"\n{int(time*1000)} ms")
                print("File berhasil disimpan ...")
            else:
                os._exit(0)
        else:
            print("Tidak ada solusi")
    else:
        matrix, sequens, h_matrix, w_matrix, buffer_size, num_seq = load_CLI()
        buffer, coor, reward, time = start(buffer_size, w_matrix, h_matrix, matrix, sequens)
        print("\nBerikut adalah matriksnya:")
        for i in range(h_matrix):
            for j in range(w_matrix):
                print(f"{matrix[i][j]}", end=" ")
            print("")
        print(f"\nAda sebanyak {len(sequens)} sequences:")
        for seq in sequens:
            for q in seq[0]:
                print(f"{q}", end=" ")
            print(f"\n{seq[1]}")
        
        print("\nHasil:")
        print(reward)
        for i in range(len(buffer)):
            print(buffer[i], end=' ')
        print()
        for j in coor:
            print(j)
        print(f"\n{int(time*1000)} ms")
        
        simpan = input("Apakah ingin menyimpan solusi? (y/n)")
        if simpan == "y":
            nama = input("Masukkan nama file: ")
            file_path = os.path.join("test\\save", nama)
            with open(file_path,"w") as file:
                file.write("\nBerikut adalah matriksnya:\n")
                for i in range(h_matrix):
                    for j in range(w_matrix):
                        file.write(f"{matrix[i][j]}")
                    file.write("\n")
                file.write(f"\nAda sebanyak {len(sequens)} sequences:\n")
                for seq in sequens:
                    for q in seq[0]:
                        file.write(f"{q}")
                    file.write(f"\n{seq[1]}\n")
                
                file.write("\nHasil:\n")
                file.write(f"{reward}\n")
                # file.write(reward)
                for i in range(len(buffer)):
                    file.write(f"{buffer[i]} ")
                file.write("\n")
                for j in coor:
                    file.write(f"{j}\n")
                file.write(f"\n{int(time*1000)} ms")
            print("File berhasil disimpan ...")
        else:
            os._exit(0)
        


if __name__ == "__main__": 
    load()
