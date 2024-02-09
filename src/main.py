# Seluruh Instruksi Utama Program
import sys
from load import load_file, load_CLI


# process
def search_col():
    ...

def search_row():
    ...

def first_step():
    search_row()

def process(buffer_size, width, height, matrix, num_seq, seqs):
    first_step(matrix[0])
    ...

# preprocess
def load():
    if len(sys.argv)>1:
        arg = sys.argv[1]
        buffer_size, width, height, matrix, num_seq, seqs = load_file(arg)
        process(buffer_size, width, height, matrix, num_seq, seqs)
        
    else:
        load_CLI()
        


if __name__ == "__main__": 
    load()



# postprocess