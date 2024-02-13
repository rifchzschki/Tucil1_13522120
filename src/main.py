# Seluruh Instruksi Utama Program
import sys
import time
import os
from load import load_file, load_CLI
from utils import *


# # process
# def search_col(matrix, col, height, goal):
#     is_found = [(-1) for k in range(len(goal))]
#     for i in range(len(goal)):
#         found=False
#         j=0
#         while(j<height and not found):
#             if matrix[j][col] == goal[i]:
#                 is_found[i] = j
#                 found=True
#             j+=1
#     return is_found 


# def search_row(matrix, width, row, goal):
#     is_found = [(-1) for k in range(len(goal))]
#     for i in range(len(goal)):
#         found=False
#         j=0
#         while(j<width and not found):
#             if matrix[row][j] == goal[i]:
#                 is_found[i] = j
#                 found=True
#             j+=1
#     return is_found
    
# def search_path(matrix, width, height, pos_row, pos_col, temp_buffer, coor, reward, seq, seq_begin):
#     is_found = True
#     tmp_row = pos_row; tmp_col = pos_col; tmp_seq_begin = seq_begin
#     buffer = temp_buffer.copy()
#     wrong = False
#     count_found = 0
#     # print("mulai")
#     # print("ini buffer sebelum", buffer)
#     tmp_coor = []
#     seq_copy = seq[0].copy()
#     # find_and_remove_sublist(buffer, seq[0])
#     inter = find_sublist(buffer, seq[0])
#     # print(inter)
#     if len(inter)!=0:
#         if(inter[-1]==buffer[-1] and inter[0]==buffer[len(buffer)-len(inter)]):
#             seq_copy = seq_copy[len(inter):]
#     # if(len(seq_copy)==0):
#     #     break
#     # print(seq_copy)
#     while(seq_begin<len(seq_copy) and is_found):
#         if len(buffer) % 2 == 2:
#             found = search_row(matrix, width, pos_row, [seq_copy[seq_begin]])
#             if (found[0] != (-1)):
#                 buffer.append(seq_copy[seq_begin])
#                 pos_col = found[0]
#                 seq_begin+=1
#                 count_found +=1
#                 tmp_coor.append([pos_row,pos_col])
#             else:
#                 is_found = False

#         else:
#             found = search_col(matrix, pos_col, height, [seq_copy[seq_begin]])
#             if (found[0] != (-1)):
#                 buffer.append(seq_copy[seq_begin])
#                 pos_row = found[0]
#                 seq_begin+=1
#                 count_found +=1
#                 tmp_coor.append([pos_row,pos_col])
#             else:
#                 is_found = False
#         # print("ini buffer", buffer, tmp_coor)
    
#     if count_found == len(seq[0]):
#         insert_buffer(buffer, seq[0])
#         insert_buffer(coor, tmp_coor)
#         reward += seq[1]
#         seq_begin = tmp_seq_begin
#     else:
#         # print(reward, seq[1])
#         buffer = temp_buffer
#         pos_col = tmp_col
#         pos_row = tmp_row
#         seq_begin = tmp_seq_begin
#         wrong = True
    

#     return buffer,coor, pos_col, pos_row, reward, seq_begin, wrong



# def process(buffer_size, width, height, matrix, num_seq, seqs):
#     #inisiasi
#     best_buffer = []
#     best_reward = 0
#     best_coor = []
#     col = 0
#     seq_begin = 0
#     while(col < width): # pengecekan dilakukan sebanyak jumlah kolom
#         reward = 0
#         temp_buffer = []
#         temp_coor = []
#         row_tmp = 0; col_tmp = col
#         if matrix[0][col]=="BD":
#             seq_begin += 1
#         temp_coor.append([0,col])
#         temp_buffer.append(matrix[0][col])
#         count_wrong = 0
#         print("col",col)
#         # print("buffer awal:",temp_buffer)
#         while(len(temp_buffer)<buffer_size and count_wrong < len(seqs)):
#             # k=0;found=True
#             # min_length = min(len(sublist) for sublist in seqs_without_reward)
#             for seq in (seqs):
#                 print("pengecekan seq", seq)
#                 if (buffer_size-len(temp_buffer))>=len(seq[0]):
#                     temp_buffer, temp_coor, col_tmp, row_tmp, reward, seq_begin, wrong = search_path(matrix, width, height, row_tmp, col_tmp, temp_buffer, temp_coor, reward, seq, seq_begin)
#                     if wrong:
#                         count_wrong +=1
#                     else:
#                         count_wrong = 0
#                 else:
#                     count_wrong +=1
            
#             # print("setelah pengecekan",temp_buffer)
#             # print(reward)

#         if len(temp_buffer)==buffer_size and best_reward<reward:
#             best_buffer = temp_buffer
#             best_reward =  reward
#             best_coor = temp_coor
        
#         col+=1
#     return best_buffer, best_reward, best_coor

def process(matrix, h_matrix, w_matrix, checked, temp_buffer, buffer_size, seq, temp_path, x, y, direction):
    global rew, buffer, path
    
    if len(temp_buffer) > buffer_size:
        return
    
    current_reward = 0
    for i in range(len(seq)):
        for j in range(len(temp_buffer) - len(seq[i][0]) + 1):
            t = temp_buffer[j:j+len(seq[i][0])]
            if t == seq[i][0]:
                current_reward += seq[i][1]
    
    if current_reward > rew:
        rew = current_reward
        buffer = temp_buffer[:]
        path = temp_path[:]
    
    token = matrix[y][x]
    if direction == 0:
        for i in range(h_matrix):
            temp_buffer.append(token)
            temp_path.append((x, y))
            checked[y][x] = 1
            if checked[i][x] == 0:
                process(matrix, h_matrix, w_matrix, checked,temp_buffer, buffer_size, seq, temp_path, x, i, 1)
            checked[y][x] = 0
            temp_buffer.pop()
            temp_path.pop()
    else:
        for i in range(w_matrix):
            temp_buffer.append(token)
            temp_path.append((x, y))
            checked[y][x] = 1
            if checked[y][i] == 0:
                process(matrix, h_matrix, w_matrix, checked,temp_buffer, buffer_size, seq, temp_path, i, y, 0)
            checked[y][x] = 0
            temp_buffer.pop()
            temp_path.pop()

def start(buffer_size, width, height, matrix, num_seq, seqs):
    global rew, buffer, path
    checked = [[0] * width for _ in range(height)]
    buffer = []
    path = []
    optimal_buff = None
    optimal_path = None
    optimum_reward = 0
    start_time = time.time()
    for i in range(width):
            rew = 0
            process(matrix, height, width, checked, buffer, buffer_size, seqs, path, i, 0, 0)
            # print(buffer)
            if rew > optimum_reward:
                optimum_reward = rew
                optimal_buff = buffer
                optimal_path = path
                # print(optimum_reward)
                # print(optimal_buff)
                # print(optimal_path)
    end_time = time.time()
    return optimal_buff, optimal_path, optimum_reward, (end_time-start_time)

# preprocess
def load():
    if len(sys.argv)>1:
        arg = sys.argv[1]
        buffer_size, width, height, matrix, num_seq, seqs = load_file(arg)
        # buffer, reward, coor = process(buffer_size, width, height, matrix, num_seq, seqs)
        buffer, coor, reward, time = start(buffer_size, width, height, matrix, num_seq, seqs)
        if (len(buffer)!=0):
            # print (buffer, reward, coor)
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
        buffer, coor, reward, time = start(buffer_size, w_matrix, h_matrix, matrix, num_seq, sequens)
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



# postprocess