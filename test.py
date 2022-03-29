#Calcular factorial
'''dfharhadhfahdfhadfhadf
adhahafdhadfhadfhadf'''
def calcularFac (num):

    numaux = 0
    if (num < 1):
        numaux = 1
    else:
        numaux = num * (calcularFac(num-1))
    return numaux
ventas = [100,200,300,400,500]

#promedio de elementos
def promedio(cualquierarreglo):
    tam = len(cualquierarreglo)
    resultado=0
    #ciclo para recorrer arreglo
    cont = 0
    sumatoria = 0
    while (cont <= tam-1):
        sumatoria = sumatoria + cualquierarreglo[cont]
        cont = cont + 1
    if tam > 0:
        resultado = sumatoria / tam
    else:
        print("Soy genial")
    return resultado

def calcularpromedioventas():
    prom = promedio(ventas)
    print("El promedio de las ventas es: ")
    print(prom)

print("Calculo del Factorial: " + calcularFac(6))
calcularpromedioventas()