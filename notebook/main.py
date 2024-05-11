import sys
sys.path.append('./libs')
from neuronas import Neurona_McCullochPittss_Todo_en_1

def main():
    # D.1.1
    # (a. -)
    tiempo_libre = 1
    motivacion = 0
    suscripcion = 0
    
    neurona = Neurona_McCullochPittss_Todo_en_1(tiempo_libre, motivacion, suscripcion)
    descision = neurona.activacion()
    
    neuronas = Neurona_McCullochPittss_Todo_en_1()
    print(neuronas.threshold) 
    
    if descision == 1:
        print("Si, ir a hacer ejercicios")
    if descision == 0:
        print("No hacer ejercicios")
    
    if __name__ == "__main__":
        main()


