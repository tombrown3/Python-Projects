
n=input('Enter a number:')
def fibonacci(n):
   n1, n2 = 0,1
   i = 0
   x = list()
   if n<=0:
      print('enter a positive integer')
   elif n==1:
       x.append(n1)
       print(x)
   else:
      print('Fibonacci sequence:')
      x.append(n1)
      x.append(n2)
      while i<n-2:
          nth = n1 + n2
          x.append(nth)
          n1 = n2
          n2 = nth
          i += 1
      print(x)

fibonacci(n)
