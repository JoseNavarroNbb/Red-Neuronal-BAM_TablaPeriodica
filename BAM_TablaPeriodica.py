import numpy as np 
  
# Tome dos conjuntos de patrones:
# Conjunto X: Patrón de entrada
h = np.array([1, 1, 1, 1, 1, 1]).reshape(6, 1) 
e = np.array([-1, -1, -1, -1, -1, -1]).reshape(6, 1) 
l = np.array([1, 1, -1, -1, 1, 1]).reshape(6, 1) 
b = np.array([-1, -1, 1, 1, -1, -1]).reshape(6, 1) 
i = np.array([1, 1, 1, 1, -1, -1]).reshape(6, 1) 
c = np.array([1, 1, 1, -1, -1, -1]).reshape(6, 1) 
n = np.array([1, 1, -1, -1, -1, -1]).reshape(6, 1)
o = np.array([-1, -1, 1, 1, 1, 1]).reshape(6, 1)
f = np.array([-1, -1, -1, 1, 1, 1]).reshape(6, 1)
  
# Conjunto Y: Patrón de destino
h1 = np.array([1, 1, 1, 1]).reshape(4, 1) 
e1 = np.array([-1, -1, -1, -1]).reshape(4, 1) 
l1 = np.array([1, -1, 1, -1]).reshape(4, 1) 
b1 = np.array([-1, 1, -1, 1]).reshape(4, 1)
i1 = np.array([1, 1, -1, 1]).reshape(4, 1) 
c1 = np.array([1, 1, -1, -1]).reshape(4, 1)  
n1 = np.array([1, -1, -1, -1]).reshape(4, 1)
o1 = np.array([-1, 1, 1, -1]).reshape(4, 1)
f1 = np.array([-1, 1, 1, 1]).reshape(4, 1)
 

# Calcular la matriz de pesos: W
x = np.concatenate((h, e, l, b, i, c, n, o, f), axis = 1) 
y = np.concatenate((h1.T, e1.T, l1.T, b1.T, i1.T, c1.T, n1.T, o1.T, f1.T), axis = 0) 
print("\nMatriz de pesos:") 
print("__________________________________________________________\n") 

w = np.dot(x, y) 
print(w)
  
print("\n__________________________________________________________\n") 
  
# Fase de prueba
# Prueba de patrones de entrada: ajuste X

def conj_X_W(x, w): 
  # Multiplica el patrón de entrada con la matriz de peso
  # (peso T X x)
  y = np.dot(w.T, x) 
  y[y < 0] = -1
  y[y >= 0] = 1
  return np.array(y) 

# Prueba de patrones de destino: conjunto Y
def conj_Y_W(y, w): 
  # Multiplica el patrón objetivo con la matriz de peso
  # (peso X y)
  x = np.dot(w, y) 
  x[x <= 0] = -1
  x[x > 0] = 1
  return np.array(x) 


while(1):
 print("Ingresa Nombre o Simbolo del elemento ***** Salir = exit ")
 answer = input()
 print("\n\n PatronRecuperado    SÍMBOLO    NOMBRE  ")


 if(answer == 'exit'):
  break

 elif(answer == 'H' or answer == 'Hidrogeno'):
     print(conj_Y_W(h1, w), '\t\t\t\t\t H \t\t Hidrogeno \n\n' ) 
 
 elif(answer == 'He' or answer == 'Helio'):
     print(conj_Y_W(h1, w),'\n',conj_Y_W(e1, w), '\t\t\t\t\t He \t\t Helio \n\n') 
  
 elif(answer == 'Li' or answer == 'Litio'):
     print(conj_Y_W(l1, w),'\n',conj_Y_W(i1, w), '\t\t\t\t\t Li \t\t Litio \n\n')

 elif(answer == 'Be' or answer == 'Berilio'):
     print(conj_Y_W(b1, w),'\n',conj_Y_W(e1, w), '\t\t\t\t\t Be \t\t Berilio \n\n')
     
 elif(answer == 'B' or answer == 'Boro'):
     print(conj_Y_W(b1, w), '\t\t\t\t\t B \t\t Boro \n\n')
     
 elif(answer == 'C' or answer == 'Carbono'):
     print(conj_Y_W(c1, w), '\t\t\t\t\t C \t\t Carbono \n\n')
     
 elif(answer == 'N' or answer == 'Nitrogeno'):
     print(conj_Y_W(n1, w), '\t\t\t\t\t N \t\t Nitrogeno \n\n')
     
 elif(answer == 'O' or answer == 'Oxigeno'):
     print(conj_Y_W(o1, w), '\t\t\t\t\t O \t\t Oxigeno \n\n')
     
 elif(answer == 'F' or answer == 'Fluor'):
     print(conj_Y_W(f1, w), '\t\t\t\t\t F \t\t Fluor \n\n')
     
 elif(answer == 'Ne' or answer == 'Neon'):
     print(conj_Y_W(n1, w),'\n',conj_Y_W(e1, w), '\t\t\t\t\t Ne \t\t Neón \n\n')
          
 else:
      print("NOMBRE O SIMBOLO DE ELEMENTO INCORRECTO\n\n")
     
     

