#este  programa realiza la tecnica de minimos cuadrados
#lista de X y Y
x=[1,2,3,4,5]
y=[4,7,9,12,16]
#tamaño de x y y
n=len (x)
#suma de valores de x
sumax=0
for i in range (n):
    xv=x[i]
    sumax=sumax+xv
#suma de valores de y
sumay=0
for i in range (n):
    yv=x[i]
    sumay=sumay+xv
#print ("sumax={}".format(sumax))
#print ("sumay={}".format(sumay))
#suma de valores de x por y
sumaxy=0
for i in range (n):
    xv=x[i]
    yv=y[i]
    producto=xv*yv
    sumaxy=sumaxy+producto
print ("sumaxy={}".format (sumaxy))
#la suma de x al cuadrado
sumax2=0
for i in range (n):
    xv=x[i]
    producto=xv*xv
    sumax2=sumax2+producto
print ("sumax2={}".format (sumaxy))
#promedio de x
promx=sumay/n
#promedio de y
promy=sumay/n
