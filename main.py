"""
======TAREAS======
- [ ] Comentar codigo
- [ ] Mirar de ver que hacer con datos invalidos (Opcional)
==================
"""

from lectorCSV import LectorCSV
from sqlConector import SQLConector

def main():
    flag = True  
    lcsv = LectorCSV()
    sql = SQLConector()
    
    print("==========================================")  
    print("=====Lector de CSV y cargador a MySQL=====")
    print("==========================================")
    try:            
        
        print("\n====Introduzca los datos de la base de datos====")
        #Preguntar datos de la base de datos
        user = input("-Introduce el usuario de la base de datos -> ")
        password = input("-Introduce la contraseña de la base de datos -> ")
        host = input("-Introduce el host de la base de datos -> ")
        nombreBD = input("-Introduce el nombre de la base de datos -> ")
        
        if not sql.conexion(user,password,host,nombreBD):
            raise ValueError ("No se ha podido conectar a la base de datos")
        
        print("===Base de datos conectada===\n")
        
        while flag:
        # Comprobamos que el fichero existe
            fileName = input("-Introduce el nombre del fichero .csv -> ")
            
            if not lcsv.leerfichero(fileName):
                raise ValueError ("El fichero donde estan ubicados los datos no existe")
            elif ".csv" not in fileName:
                raise ValueError ("El fichero no es un .csv")
            print("Procesando informacion del csv...")
            
            columnas = lcsv.getColumns()
            typeColumns = lcsv.getcolumsTypes()
            datos = lcsv.getRows()
            
            while True:
                optionTable = input("¿Desea crear una nueva tabla o insertar en una ya existente? (N/I) -> ")
                
                if optionTable == "N" or optionTable == "n":
                    name = input("-Que nombre quieres darle a la tabla? ")
                    if  not sql.createTable(name,typeColumns,columnas,datos):
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
            
            while True:
                option = input("-Quieres insertar mas datos? (s/n) -> ")
                if option=="n" or option=="N":
                    flag = False
                    break
                elif option=="s" or option=="S":
                    break
                else:
                    print("Error, opcion no valida")
             
    except ValueError as Error:#Captador de errores
        print("Error:",Error)
    

if __name__ == "__main__":
    main()