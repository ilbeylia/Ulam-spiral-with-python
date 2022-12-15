import numpy as np
import matplotlib.pyplot as plt



size = 10

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

sayilar = np.zeros(size**2)
test = spiral(sayilar.reshape(size,size))
test = np.hstack (test)


n = 10
matrix =  [ [0 for i in range(n)] for j in range (n)]

x = []
y = []

for i in test:
    if i == 90 :
        x.append(i % n) 
        y.append(9)
    else:
        x.append(i % n) 
        y.append((i // n))

def asal(değer):
    if değer>2:
        for t in range(2,değer):
            if (değer % t) == 0: 
                asalD = 0
            else:
                asalD = 1     
    else:
        asalD = 1
    return asalD

test = asal(17)
print(test)


for a in range(100):
        matrix[x[a]][y[a]] = a+1



matrix = np.array(matrix)
matrix = matrix.reshape(n,n)

print(matrix)








