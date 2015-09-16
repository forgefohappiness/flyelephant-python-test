from time import time

def fibonacci(n):
   if(n==0):
     return 0
   if(n==1):
     return 1 
   return fibonacci(n-1)+fibonacci(n-2)

file = open('result.csv','w')

file.write("Iteration,Value,Seconds\n")

for i in range(35):
   point1 = time()
   fib = fibonacci(i)
   point2 = time()
   file.write(str(i)+","+str(fib)+","+str(point2-point1)+"\n")

file.close()
