from time import time

def fibonacci(n):
   if(n==0):
     return 0
   if(n==1):
     return 1 
   return fibonacci(n-1)+fibonacci(n-2)

file = open('result.dat','w')


for i in range(30,40):
   point1 = time()
   fib = fibonacci(i)
   point2 = time()
   file.write(str(i)+"-i fib number tooks "+str(point2-point1)+" sec\n")

file.close()
