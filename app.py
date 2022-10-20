"""
======TAREAS======
- [ ] Mirar de ver que hacer con datos invalidos (Opcional)
==================
"""

from lectorCSV import LectorCSV
from sqlConector import SQLConector
from pathlib import Path
import getpass

def main():
    flag = True # Flag para controlar el bucle
      
    # Declaracion de objetos
    lcsv = LectorCSV()
    sql = SQLConector()
    
    print("==========================================")  
    print("=====Conversor de CSV a BD de MySQL=====")
    print("==========================================")
    try:            
        
        print("\n====Introduzca los datos de la base de datos====")
        
        #Preguntamos datos de la base de datos
        user = input("-Introduce el usuario de la base de datos -> ")
        password = getpass.getpass("-Introduce la contraseña de la base de datos -> ")
        host = input("-Introduce el host de la base de datos -> ")
        nombreBD = input("-Introduce el nombre de la base de datos -> ")
        
        # Comprobamos que la conexion es correcta
        if not sql.conexion(user,password,host,nombreBD):
            raise ValueError ("No se ha podido conectar a la base de datos")
        
        print("===Base de datos conectada===\n")
        
        #Bucle para que el usuario pueda cargar varios ficheros
        while flag:
            
            fileName = input("-Introduce el nombre del fichero .csv -> ")
            
            if ".csv" not in fileName:# Comprobamos que el fichero es .csv
                raise ValueError ("El fichero no es un .csv")
            
            if not lcsv.leerfichero(Path("data",fileName)):#Comprobamos que el fichero existe
                raise ValueError ("El fichero donde estan ubicados los datos no existe")
            
            print("Procesando informacion del csv...")
            
            # Cogemos las columnas, los tipos de datos de cada columna y los datos
            columnas = lcsv.getColumns()
            typeColumns = lcsv.getcolumsTypes()
            datos = lcsv.getRows()
            
            # Bucle para crear la tabla o insertar los datos
            while True:
                # Preguntamos si queremos crear la tabla o insertar los datos
                optionTable = input("¿Desea crear una nueva tabla o insertar en una ya existente? (N/I) -> ")
                
                if optionTable == "N" or optionTable == "n":
                    name = input("-Que nombre quieres darle a la tabla? ")
                    if  not sql.createTable(name,typeColumns,columnas,datos):
                        raise ValueError ("No se ha podido insertar los datos en la base de datos")
                    if  not sql.insertInTable(name,columnas,typeColumns,datos):
                        raise ValueError ("No se ha podido insertar los datos en la base de datos")
                    break
                elif optionTable == "I" or optionTable == "i":
                    name = input("-En que tabla quieres insertar los datos? ")
                    if  not sql.insertInTable(name,columnas,typeColumns,datos):
                        raise ValueError ("No se ha podido insertar los datos en la base de datos")
                    break
                else:
                    print("Error, opcion no valida")
                    
            print("===Datos insertados correctamente===\n")
            
            #Bucle para preguntar si queremos cargar otro fichero
            while True:
                option = input("-Quieres insertar mas datos? (s/n) -> ")
                if option=="n" or option=="N":
                    print("=======================")
                    print("======HASTA LUEGO======")
                    print("=======================")
                    flag = False
                    break
                elif option=="s" or option=="S":
                    break
                else:
                    print("Error, opcion no valida")
             
    # Controlamos las excepciones
    except ValueError as Error:
        print("Error:",Error)
    

if __name__ == "__main__":
    main()