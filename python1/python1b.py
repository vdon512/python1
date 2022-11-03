try:
    num=int(input("Escribe un número: "))
    if num < 0:
        raise Exception("{num} es negativo")
    for i in range(0,num,2):
        print(i,end=" ")
except ValueError as e:
    print("errior")
except KeyboardInterrupt as e2:
    print(e2)
except:
    print("exception genérica")
    

"""
while True:
    nombre=input("¿Cómo te llamas? ")
    if nombre == "":
        print("No has escrito nada",end=" ...")
    else:
        print("Hola "+ nombre + " encantado",end=" ---")
        print("Adiós")
        break;
"""