import csv
import random as rd
import statistics
def asignar_sueldos(trabajadores):
    sueldos_trabajadores={}
    for trabajador in trabajadores:
        sueldo = rd.randint(300000,2500000)
        sueldos_trabajadores[trabajador]= sueldo
    return sueldos_trabajadores

def clasificar_sueldos(sueldos_trabajadores):
    menor_800={}
    entre_800_2m={}
    superior_2m={}
    for trabajador,sueldo in sueldos_trabajadores.items():
        if sueldo < 800000:
            menor_800[trabajador]=sueldo
        else:
            if sueldo > 800 and sueldo <= 2000000:
                entre_800_2m[trabajador]=sueldo
            else:
                if sueldo > 2000000:
                    superior_2m[trabajador]=sueldo
    print("Sueldos menores a 800.000 TOTAL: ",len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print("Nombre del trabajador: ",trabajador,", Sueldo: ",sueldo)
    print("Sueldos entre 800.000 y 2.000.000 TOTAL: ",len(entre_800_2m))
    for trabajador,sueldo in entre_800_2m.items():
        print("Nombre del trabajador: ",trabajador,", Sueldo: ",sueldo)
    print("Sueldos superiores a 2.000.000 TOTAL: ",len(superior_2m))
    for trabajador,sueldo in superior_2m.items():
        print("Nombre del trabajador: ",trabajador,", Sueldo: ",sueldo)

def estadisticas(sueldos_trabajadores):
    sueldo = list(sueldos_trabajadores.values())
    sueldo_alto=max(sueldo)
    sueldo_bajo=min(sueldo)
    promedio_sueldo=sum(sueldo)/len(sueldo)
    media=statistics.geometric_mean(sueldo)
    return sueldo_alto,sueldo_bajo,promedio_sueldo,media

def generar_reporte_sueldos(sueldo_trabajadores):

    with open("reporte_sueldos.csv","w") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["Nombre empleado","Sueldo base","Descuento salud","Descuento AFP","Sueldo liquido"])
        for trabajador,sueldo in sueldo_trabajadores.items():
            escritor.writerow([trabajador,sueldo,sueldo*0.07,sueldo*0.12,sueldo-(sueldo*0.07+sueldo*0.12)])