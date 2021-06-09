ejecutar = True

menu = """ Bienvenido al conversos de monedas, que deseas?
🥇De dolares a pesos [1] o 
de pesos a dolares [2] o
salir[3]? 😁 
"""

def conversor(Eleccion):
 global ejecutar 
 valor_dolar = 3616.12

 if Eleccion == 1:
     moneda_a_convertir = float(input("Cuantos dolares tienes?:"))
     moneda_a_convertir = moneda_a_convertir * valor_dolar
     moneda = "Pesos colombianos"

 elif Eleccion == 2:
     moneda_a_convertir = float(input("Cuantos pesos colombianos tienes?:"))
     moneda_a_convertir = moneda_a_convertir / valor_dolar
     moneda = "Dolares"
 
 elif Eleccion == 3:
     ejecutar = False
     print("Adios")
     return
 else:
       print("No mames, escoge una opcion correcta")
       return

 moneda_a_convertir = round(moneda_a_convertir, 2)
 print(f'Tu tienes ${moneda_a_convertir} {moneda}')

if __name__ == '__main__':
     while(ejecutar):
         try:
             Eleccion = int(input(menu))
         except:
             Eleccion = str(input(menu))   
     conversor(Eleccion)

    