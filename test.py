#Calcular factorial
def calcularFac(num):
    num_aux = 0
    if (num < 1):
        num_aux = 1
    else:
        num_aux = num * (calcularFac(num-1))
    return num_aux

ventas = [100,200,300,400,500]

#promedio de elementos
def promedio(cualquier_arreglo):
    tam = len(cualquier_arreglo)
    resultado=0
    #ciclo para recorrer arreglo
    cont = 0
    sumatoria = 0
    while (cont <= tam-1):
        sumatoria = sumatoria + cualquier_arreglo[cont]
        cont += 1
    if tam > 0:
        resultado = sumatoria / tam
    return resultado

def calcularpromedioventas():
    prom = promedio(ventas)
    print("El promedio de las ventas es: ")
    print(prom)

print("Calculo del Factorial: " + calcularFac(6))
calcularpromedioventas()