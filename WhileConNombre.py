menu = """ 
Buenas, vas a responder una encuesta, 
escribe tu nombre:"""


ejecutar = True
n = 0
nombre_completo = ""

def buenas_mayusculas(i):
    global n
    global nombre_completo
    while(n < i):
        nombre_completo += nombre[n:n+1]
        if nombre[n:n+1] == " ":
             nombre_completo += nombre[n+1:n+2].upper()
             n += 1
        n += 1
    return print(nombre_completo)         

        
if __name__ == '__main__':
    nombre = str(input(menu))
    nombre = nombre.capitalize()
    buenas_mayusculas(len(nombre))

         



