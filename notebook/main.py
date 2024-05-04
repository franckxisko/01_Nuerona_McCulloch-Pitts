import sys
sys.path.append('./libs')
from neuronas import Neurona_McCullochPittss_Todo_en_1

def main():
    neuronas = Neurona_McCullochPittss_Todo_en_1()
    print(neuronas.threshold) 
    
    if __name__ == "__main__":
        main()


