# import numpy as np

# def text_correction(matrix):  
#     m = matrix
#     m = m.split('\n')[:-1]
#     for i in range(len(m)):
#         m[i] = m[i].split()
#         for j in range(len(m[i])):
#             if (m[i][j].find('c') != -1 or m[i][j].find('C') != -1 or
#                 m[i][j].find('i') != -1 or m[i][j].find('t') != -1 or
#                 m[i][j].find('1') != -1 or m[i][j].find('W') != -1 or
#                 m[i][j].find('w') != -1 or m[i][j].find('©') != -1):
#                 m[i][j]= "1C"

#             if (m[i][j].find('€') != -1 or m[i][j].find('9') != -1 or
#                 m[i][j].find('E') != -1 or m[i][j].find('e') != -1 or
#                 m[i][j].find('o') != -1):
#                 m[i][j]= "E9"

#             if (m[i][j].find('B') != -1 or m[i][j].find('D') != -1 or
#                 m[i][j].find('O') != -1 or m[i][j].find('0') != -1):
#                 m[i][j]= "BD"

#             if (m[i][j].find('5') != -1 or m[i][j].find('§') != -1 or
#                 m[i][j].find('S') != -1 or m[i][j].find('6') != -1):
#                 m[i][j]= "55"
#     return m

# def visit(m,visited,cursor,row, buffer, sequence, seq_index):
#     if row == True:
#         nv = sequence[seq_index] in m[cursor["x"]]
#         if nv == True:
#             where = np.where(m[cursor["x"]] == sequence[seq_index])[0]
#         else:
#             where = []
#         for i in where:        
#             if visited[cursor["x"]][i] == 0:               
#                 cursor["y"] = i
#                 buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                 buffer["path"].append((cursor["x"],cursor["y"]))
#                 visited[cursor["x"]][cursor["y"]] = 1
#                 seq_index += 1
#                 row = False
#                 return visited, cursor, row, buffer, seq_index
#          # If all neighbors visited
#         if seq_index > 1:
#             # Then go back to the last position
#             buffer["simbols"].pop()
#             buffer["path"].pop()
#             cursor["x"] = buffer["path"][-1][0]
#             cursor["y"] = buffer["path"][-1][1]
#             seq_index -= 1
#             row = False
#             return visited, cursor, row, buffer, seq_index

#         elif seq_index == 1:
#             where = np.where(m[cursor["x"]] == sequence[seq_index-1])[0]
#             # Visiting the not visited neighbors
#             for i in where:
#                 if visited[cursor["x"]][i] == 0:               
#                     cursor["y"] = i
#                     buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                     buffer["path"].append((cursor["x"],cursor["y"]))
#                     visited[cursor["x"]][cursor["y"]] = 1
#                     # Do not upgrade seq_index
#                     row = False
#                     return visited, cursor, row, buffer, seq_index
#             # If no neighbor avaliable go back
#             buffer["simbols"].pop()
#             buffer["path"].pop()
#             cursor["x"] = buffer["path"][-1][0]
#             cursor["y"] = buffer["path"][-1][1]
#             #seq_index -= 1
#             row = False
#             return visited, cursor, row, buffer, seq_index

#         elif seq_index == 0:
#             for i in range(len(m[cursor["x"]])):
#                 if visited[cursor["x"]][i] == 0:
#                     cursor["y"] = i
#                     buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                     buffer["path"].append((cursor["x"],cursor["y"]))
#                     visited[cursor["x"]][cursor["y"]] = 1
#                     row = False
#                     return visited, cursor, row, buffer, seq_index

#         else:
#             # OK, that sequence dont exist on the matrix
#             print("ERROR")
#     else:
#         nv = sequence[seq_index] in m[:,cursor["y"]]
#         if nv == True:
#             where = np.where(m[:, cursor["y"]] == sequence[seq_index])[0]
#         else:
#             where = []
#         for i in where:
#             if visited[i][cursor["y"]] == 0:
#                 cursor["x"] = i
#                 buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                 buffer["path"].append((cursor["x"],cursor["y"]))
#                 visited[cursor["x"]][cursor["y"]] = 1
#                 seq_index += 1
#                 row = True
#                 return visited, cursor, row, buffer, seq_index
#         # If all neighbors visited
#         if seq_index > 1:
#             # Then go back to the last position
#             buffer["simbols"].pop()
#             buffer["path"].pop()
#             cursor["x"] = buffer["path"][-1][0]
#             #cursor["y"] = buffer["path"][-1][1]
#             seq_index -= 1
#             row = True
#             return visited, cursor, row, buffer, seq_index

#         elif seq_index == 1:
#             where = np.where(m[:, cursor["y"]] == sequence[seq_index-1])[0]
#             # Visiting the not visited neighbors
#             for i in where:
#                 if visited[i][cursor["y"]] == 0:               
#                     cursor["x"] = i
#                     buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                     buffer["path"].append((cursor["x"],cursor["y"]))
#                     visited[cursor["x"]][cursor["y"]] = 1
#                     # Do not upgrade seq_index
#                     row = True
#                     return visited, cursor, row, buffer, seq_index
#             # If no neighbor avaliable go back
#             buffer["simbols"].pop()
#             buffer["path"].pop()
#             #cursor["x"] = buffer["path"][-1][0]
#             #cursor["y"] = buffer["path"][-1][1]
#             seq_index -= 1
#             row = True
#             return visited, cursor, row, buffer, seq_index

#         elif seq_index == 0:
#             for i in range(len(m[:,cursor["y"]])):
#                  if visited[i][cursor["y"]] == 0:
#                     cursor["x"] = i
#                     buffer["simbols"].append(m[cursor["x"]][cursor["y"]])
#                     buffer["path"].append((cursor["x"],cursor["y"]))
#                     visited[cursor["x"]][cursor["y"]] = 1
#                     row = True
#                     return visited, cursor, row, buffer, seq_index

#         else:
#             # OK, that sequence dont exist on the matrix
#             print("ERROR")

# def solver(matrix, sequence):
#     '''
#     Solves one sequence
#     ''' 
#     BUFFER_SIZE = 6
#     seq_index = 0
#     visited = np.array(matrix)
#     visited = np.zeros(visited.shape)
#     row = True
#     cursor = {"x": 0, "y": 0}
#     buffer = {"simbols":[],"path":[]}
#     while len(buffer['path']) <= BUFFER_SIZE and seq_index < len(sequence):
#         visited, cursor, row, buffer, seq_index = visit(matrix, visited, cursor, row, buffer, sequence, seq_index)
#     print(f'sequence: {buffer["simbols"]}')
#     print(f'path: {buffer["path"]}')
#     return buffer["path"]



# if __name__ == "__main__":
#     matrix = np.array([["7A", "BD", "55", "55", "1C", "1C"],
#                        ["7A", "1C", "55", "E9", "1C", "7A"],
#                        ["7A", "7A", "1C", "7A", "55", "E9"],
#                        ["1C", "7A", "BD", "1C", "BD", "1C"],
#                        ["BD", "E9", "1C", "7A", "1C", "7A"]])
#     sequence = ["55", "7A" ,"55"]
#     solver(matrix, sequence)
# -----------------------------------------------------------------------
def find_paths(matrix, row, col, path_length, current_path, path_coordinates, visited, is_horizontal):
    if path_length == 7:
        paths.append((current_path.copy(), path_coordinates.copy()))  # Menambahkan path dan koordinatnya ke daftar hasil
        return

    if is_horizontal:
        # Pergerakan horizontal ke kanan
        if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
            visited[row][col + 1] = True
            find_paths(matrix, row, col + 1, path_length + 1, current_path + [matrix[row][col + 1]], path_coordinates + [(row, col + 1)], visited, not is_horizontal)
            visited[row][col + 1] = False

        # Pergerakan horizontal ke kiri
        if col > 0 and not visited[row][col - 1]:
            visited[row][col - 1] = True
            find_paths(matrix, row, col - 1, path_length + 1, current_path + [matrix[row][col - 1]], path_coordinates + [(row, col - 1)], visited, not is_horizontal)
            visited[row][col - 1] = False
    else:
        # Pergerakan vertikal ke bawah
        if row < len(matrix) - 1 and not visited[row + 1][col]:
            visited[row + 1][col] = True
            find_paths(matrix, row + 1, col, path_length + 1, current_path + [matrix[row + 1][col]], path_coordinates + [(row + 1, col)], visited, not is_horizontal)
            visited[row + 1][col] = False

        # Pergerakan vertikal ke atas
        if row > 0 and not visited[row - 1][col]:
            visited[row - 1][col] = True
            find_paths(matrix, row - 1, col, path_length + 1, current_path + [matrix[row - 1][col]], path_coordinates + [(row - 1, col)], visited, not is_horizontal)

            visited[row - 1][col] = False

# Inisialisasi daftar hasil
paths = []

# Matriks yang diberikan
matrix = [
    ['7A', '55', 'E9', 'E9', '1C', '55'],
    ['55', '7A', '1C', '7A', 'E9', '55'],
    ['55', '1C', '1C', '55', 'E9', 'BD'],
    ['BD', '1C', '7A', '1C', '55', 'BD'],
    ['BD', '55', 'BD', '7A', '1C', '1C'],
    ['1C', '55', '55', '7A', '55', '7A']
]

# Iterasi untuk mencari path yang dimulai dari setiap titik di baris pertama
for col in range(len(matrix[0])):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # Reset visited setiap iterasi
    visited[0][col] = True
    find_paths(matrix, 0, col, 1, [matrix[0][col]], [(0, col)], visited, True)
    visited[0][col] = False

# Cetak hasil path
for path, coordinates in paths:
    print("Path:", path)
    print("Coordinates:", coordinates)
    print()




# sequences = {
#     ('BD', 'E9', '1C'): 15,
#     ('BD', '7A', 'BD'): 20,
#     ('BD', '1C', 'BD', '55'): 30
# }

# def check_sequence_in_path(path,sequences):
#     total_reward = 0  # Inisialisasi total reward
#     matched_sequences = []  # Inisialisasi daftar sequence yang cocok

#     # Iterasi melalui setiap sequence yang telah didefinisikan
#     for sequence, reward in sequences.items():
#         seq_length = len(sequence)
#         path_length = len(path)
#         # Iterasi melalui setiap token dalam path
#         for i in range(path_length - seq_length + 1):
#             # Bandingkan token dalam path dengan token dalam sequence
#             if path[i:i+seq_length] == list(sequence):
#                 # Jika sequence ditemukan dalam path, tambahkan reward dan sequence ke total_reward dan matched_sequences
#                 total_reward += reward
#                 matched_sequences.append(sequence)
#     # Kembalikan total_reward dan matched_sequences
#     return total_reward, matched_sequences

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
