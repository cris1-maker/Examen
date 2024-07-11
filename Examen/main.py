import funciones as fn
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_trabajadores={}
while True:
    try:
        print("----------MENU------------")
        print("(0) Inicializar sueldos.")
        print("(1) Asignar sueldos aleatorios.")
        print("(2) Clasificar sueldos.")
        print("(3) Ver estadisticas.")
        print("(4) Reporte de sueldo.")
        print("(5) Salir")
        opcion=int(input("Ingrese opcion: "))
        if opcion==0:
            sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}
            print("Sueldros inicializados.")
        else:
            if opcion==1:
                if not sueldos_trabajadores:
                    print("Porfavor , primero inicialize sueldos , (Opcion 0)")
                else:
                    sueldos_trabajadores=fn.asignar_sueldos(trabajadores)
            else:
                if opcion==2:
                    if sueldos_trabajadores:
                        fn.clasificar_sueldos(sueldos_trabajadores)
                    else:
                        print("Debe asignar sueldos.")
                else:
                    if opcion==3:
                        if sueldos_trabajadores:
                            sueldo_alto,sueldo_bajo,promedio_sueldo,media=fn.estadisticas(sueldos_trabajadores)
                            print("Sueldo mas alto: ",sueldo_alto)
                            print("Sueldo mas bajo: ",sueldo_bajo)
                            print("Promedio de sueldos: ",promedio_sueldo)
                            print("Media geometrica: ",media)
                        else:
                            print("Primero asigne sueldos.")
                    else:
                        if opcion==4:
                            if sueldos_trabajadores:
                                fn.generar_reporte_sueldos(sueldos_trabajadores)
                            else:
                                print("Primero asigne sueldos.")
                        else:
                            if opcion==5:
                                print("Finalizando programa... ")
                                print("Desarrolado por Cristian Rodriguez")
                                print("Rut 19.613.150-7")
                                break
                            else:
                                print("Ingrese opcion valida.")
    except ValueError:
        print("Ingrese solo numeros.")




