n = input('Enter length of the Fibonacci sequence : ')
def fibonacci(n):
    n1,n2 = 0,1
    x = list()
    i=0
    if n<=0:
        print('Enter a positive integer : ')
    elif n==1:
        x.append(n1)
        print(x)
    else:
        x.append(n1)
        x.append(n2)
        while i< n-2:
            nth= n1+n2
            x.append(nth)
            n1 = n2
            n2 = nth
            i += 1
        print(x)
fibonacci(n)
  
