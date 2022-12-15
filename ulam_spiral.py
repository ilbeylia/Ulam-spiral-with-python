import numpy as np
import matplotlib.pyplot as plt



n = 251 

def spiral(dizi):
    rows, cols = dizi.shape
    idler = np.arange(rows*cols).reshape(rows,cols)[::-1]

    spiral_id = []
    while idler.size:
        spiral_id.append(idler[0])
        idler = idler[1:]

        idler = idler.T [::-1]

    
    spiral_id = np.hstack(spiral_id)

    spiral_id= spiral_id[::-1]

    return spiral_id

sayilar = np.zeros(n**2)
test = spiral(sayilar.reshape(n,n))
test = np.hstack (test)


matrix =  [ [0 for i in range(n)] for j in range (n)]

x = []
y = []

for i in test:
    if i == (n**2 - n) :
        x.append(i % n) 
        y.append(n-1)
    else:
        x.append(i % n) 
        y.append((i // n))


def asal(değer):
    if (değer >2):
        for i in range(2,değer):
            if ((değer % i) == 0):
                asala = 0
                break
            else:
                asala = 1

    elif değer == 2:
        asala = 1
    
    else :
        asala=0

    return asala

for a in range(n**2):
    test = asal(a)
    if test == 1:
        matrix[x[a]][y[a]] = 1
        plt.plot(x[a],y[a],'o--', color = 'black', markersize = 0.5)        
    else:
        matrix[x[a]][y[a]] = 0

matrix = np.array(matrix)
matrix = matrix.reshape(n,n)

plt.axis("off")
plt.show()








