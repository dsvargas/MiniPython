"""
	Cdigo de prueba para
	# Anlisis Sintctico #


quitamos los caracteres especiales de los string como tildes

"""

#Calcular factorial
def calcularFac(num):
    num_aux = 0
    if (num < 1):
        num_aux = -1
    else:
        #el numero uno tine que estar entre parenticis para que divida las expreciones
        # si lo pone con los dos menos va a dar un error de recursion
        num_aux = num * (calcularFac(num-1))
    return num_aux

ventas = [100,200,300,400,500,-3.14]

Caracter = '%'

cualquier_arreglo= []
#promedio de elementos
def promedio(cualquier_arreglo):
    tam = len(cualquier_arreglo)
    resultado=0
    #ciclo para recorrer arreglo
    cont = 0
    sumatoria = 0
    while (cont <= tam-1):
        sumatoria = sumatoria + cualquier_arreglo[cont]
        cont = cont + 1
    if tam > 0:
        resultado = sumatoria / tam
    return resultado

def calcularpromedioventas():
    prom = promedio(ventas)#esto ocupa un arreglo para funcionar y el len me va a devolver un numero
    print("El promedio de las ventas es: ")
    #Para que no de error aqui el print tiene que estar entre comillas dobles
    # porque la regla dice que la exprecion puede ser un string
    # pero el string  debe estar entre comillas dobles
    print("\n")
    print(prom)

# no se puede concatenar de esta manera strings y numeros. lo correcto es separarlos por comas
#print("Calculo del Factorial:%$ " + calcularFac(6))
print("Calculo del Factorial:%$ "+ calcularFac(6))
calcularpromedioventas()


#a,b,c=1,2,3
