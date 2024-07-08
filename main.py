from funciones_parcial import *
import os

while True:
    os.system("cls")
    
    match menu():
        
        case "1":
            os.system("cls")
            lista_bicicletas = obtener_lista_bicicletas("bicicletas.csv")
            print("Lista cargada exitosamente")
  
        case "2":
            os.system("cls")
            try:
                mostrar_bicicletas(lista_bicicletas)
            except:
                print("La lista de bicicletas no fue cargada")
                
        case "3":
            os.system("cls")
            try:
                asignar_tiempo(lista_bicicletas)
                mostrar_bicicletas_y_dato(lista_bicicletas, "tiempo")
            except:
                print("La lista de bicicletas no fue cargada")

        case "4":
            os.system("cls")
            try:
                menor_tiempo = obtener_mejor_dato(lista_bicicletas, "tiempo")
                mostrar_bicicleta_menor_tiempo(lista_bicicletas, menor_tiempo)
            except:
                print("La lista de bicicletas no fue cargada")
    
        case "5":
            os.system("cls")
            try:
                tipo_bicicleta = input("Ingrese el tipo de bicicleta a filtrar entre MTB/Paseo/BMX/Playera: ").upper()
                while not(tipo_bicicleta == "MTB" or tipo_bicicleta == "PASEO" or tipo_bicicleta == "PLAYERA" or tipo_bicicleta == "BMX"):
                    tipo_bicicleta = input("Tipo invalido. Reingrese el tipo de bicicleta a filtrar entre MTB/Paseo/BMX/Playera: ").upper()
                
                lista_bicicletas_filtradas = filtrar_bicicletas(lista_bicicletas, tipo_bicicleta)
                crear_archivo_tipo_bicicleta(lista_bicicletas_filtradas, tipo_bicicleta.lower() + ".csv")
                print("Archivo creado exitosamente")
            except:
                print("La lista de bicicletas no fue cargada")
                
        case "6":
            os.system("cls")
            try:
                promedio_playera = obtener_promedio_tiempo_tipo(lista_bicicletas, "PLAYERA")
                promedio_bmx = obtener_promedio_tiempo_tipo(lista_bicicletas, "BMX")
                promedio_paseo = obtener_promedio_tiempo_tipo(lista_bicicletas, "PASEO")
                promedio_mtb = obtener_promedio_tiempo_tipo(lista_bicicletas, "MTB")
                
                print("El promedio de tiempo de cada tipo de bicicleta es:")
                print(f"Playera: {promedio_playera:.2f} | BMX: {promedio_bmx:.2f} | Paseo: {promedio_paseo:.2f} | MTB: {promedio_mtb:.2f}")
            except:
                print("La lista de bicicletas no fue cargada")

        case "7":
            os.system("cls")
            
            lista_playera = ordenar_bicicletas_tiempo(lista_bicicletas, "PLAYERA", "tiempo")
            promedio_bmx = ordenar_bicicletas_tiempo(lista_bicicletas, "BMX", "tiempo")
            promedio_paseo = ordenar_bicicletas_tiempo(lista_bicicletas, "PASEO", "tiempo")
            promedio_mtb = ordenar_bicicletas_tiempo(lista_bicicletas, "MTB", "tiempo")
            mostrar_bicicletas(lista_playera)
            mostrar_bicicletas(promedio_bmx)
            mostrar_bicicletas(promedio_paseo)
            mostrar_bicicletas(promedio_mtb)
            

        case "8":
            os.system("cls")
    
        case "9":
            os.system("cls")   
            break
           
    os.system("pause")
    
