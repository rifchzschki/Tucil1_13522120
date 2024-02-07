# Seluruh Instruksi Utama Program
import sys
from load import load_file, load_CLI, height_matrix




# preprocess
def main():
    if len(sys.argv)>1:
        arg = sys.argv[1]
        load_file(arg)
        
    else:
        load_CLI()
        print(height_matrix)


if __name__ == "__main__": 
    main()


# process

# postprocess