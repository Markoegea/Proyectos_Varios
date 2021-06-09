estado = int(input('Escribe una opcion: '))

def factorial(n):
    """ Calcula el factorial de n
     n int > 0
     return n!
    """
    if n==1:
     return 1
    return n * factorial(n-1 )



def fibonacci(C):
    if C==0 or C ==1:
        return 1
    return fibonacci(C-1) + fibonacci(C-2)

    
if estado == 1: 
  n = int(input('Escribe un entero: '))
  factorial(n)
  print(factorial(n))
elif estado == 2: 
  C = int(input('Escribe un mes: '))
  fibonacci(C)
  print(fibonacci(C))      
    

    