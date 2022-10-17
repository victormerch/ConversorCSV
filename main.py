"""
======TAREAS======
- [ ] Comprobar que el fichero sea .csv
- [ ] Mirar de hacer diferente el que se cree siempre una tabla nueva, 
      y el poner opcion de insertar en una tabla ya existente o crear una nueva
- [ ] Comentar codigo
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
            
            if not lcsv.leerfichero(fileName+".csv"):
                raise ValueError ("El fichero donde estan ubicados los datos no existe")
            print("Procesando informacion del csv...")
            
            columnas = lcsv.getColumns()
            typeColumns = lcsv.getcolumsTypes()
            datos = lcsv.getRows()
            
            
            name = input("-Que nombre quieres darle a la tabla? ")
            if  not sql.createTable(name,typeColumns,columnas,datos):
                raise ValueError ("No se ha podido insertar los datos en la base de datos")
            
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

