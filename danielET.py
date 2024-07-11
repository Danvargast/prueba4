import random
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []
dictSueldo = {}
def asignarSueldos(trabajadores):
    sueldos.clear()
    dictSueldo.clear()
    for i in trabajadores:
        sueldo = random.randint(300000,2500000)
        dictSueldo[sueldo] = i
        trabajador = [i,sueldo]
        sueldos.append(trabajador)
def clasificarSueldos(sueldos):
    sueldoBajo = []
    sueldoMedio = []
    sueldoAlto = []
    for a in sueldos: 
        if a[1] < 800000:
            sueldoBajo.append(a)
        elif  800000 <= a[1] <= 2000000:
            sueldoMedio.append(a)
        elif a[1] > 2000000:
            sueldoAlto.append(a)
    print(f"Los sueldos menores a $800.000 son {len(sueldoBajo)}, {sueldoBajo}, sueldos entre $800.000 y 2.000.000 {sueldoMedio}, sueldos superiores a 2.000.000 {sueldoAlto} ")
def verEstadisticas():
    bajo = min(dictSueldo.keys())
    alto = max(dictSueldo.keys())
    promedio = sum(dictSueldo.keys())/len(dictSueldo.keys())
    print(f"El sueldo más bajo es: {bajo}, el más alto es {alto} y el sueldo promedio es: {promedio}")

def reporteSueldos():
    reporte = {}
    for n in dictSueldo.keys():
        descuentoSalud = n * 0.07
        descuentoAFP = n*0.12
        sueldoLiquido = n - descuentoAFP - descuentoSalud
        nombre = dictSueldo.get(n)
        reporte [nombre] = f"Sueldo: ${n} Descuento salud: ${descuentoSalud} Descuento AFP: ${descuentoAFP} sueldo líquido: ${sueldoLiquido}"
    for a in reporte.items():
        print(a)
while True:
    print("""¿Qué desea hacer?(escribe el número)
1.Asignar sueldos aleatorios 
2.Clasificar sueldos
3.Ver estadísticas
4.Reporte de sueldos
5.Salir""")
    opcion = int(input(""))
    if opcion == 1:
        asignarSueldos(trabajadores)
        for sueldo in sueldos:
            print(sueldo)
    if opcion == 2:
        clasificarSueldos(sueldos)
    if opcion == 3:
        verEstadisticas()
    if opcion == 4:
        reporteSueldos()
    if opcion == 5:
        print("Finalizando programa...")
        print("Desarrollado por Daniel Vargas")
        print("Rut 21.339.629-3")
        break
    
    input("presiona cualquier tecla para continuar en el menú: ")