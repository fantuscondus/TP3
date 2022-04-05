def primes (n):

#n= input("donneer un numero  ")

    for i in range (2,n):

      if(n % i) ==0:

        break

    else :

       print (i)

primes(10)