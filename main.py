"""
======TAREAS======
- [ ] Implementar try and catch para los posibles errores, MEDIO Hecho
      Pedir datos de la base de datos y comprobar que estos se pongan bien por teclado
- [ ] Comentar codigo
==================
"""

from lectorCSV import LectorCSV
from sqlConector import SQLConector

def main():
    print("=====Lector de CSV y cargador a MySQL=====")
    lcsv = LectorCSV()
    sql = SQLConector()
    try:
        fileName = input("-Introduce el nombre del fichero -> ")

        # Comprobamos que el fichero existe
        if not lcsv.leerfichero(fileName+".csv"):
            raise ValueError ("El fichero donde estan ubicados los datos no existe")
        print("Procesando informacion del csv...")
        
        #Preguntar datos de la base de datos
        
        if not sql.conexion("root","test","localhost","IABD"):
            raise ValueError ("No se ha podido conectar a la base de datos")
        
        print("Base de datos conectada...")
        
        columnas = lcsv.getColumns()
        typeColumns = lcsv.getcolumsTypes()
        datos = lcsv.getRows()
        print("Insertando datos en la base de datos...")
        
        name = input("Que nombre quieres darle a la tabla? ")
        if sql.createTable(name,typeColumns,columnas,datos):
            print("Datos insertados correctamente")
            
        else:
            print("Error en la conexion")
        
            
    except ValueError as Error:#Captador de errores
        print("Error:",Error)
    

if __name__ == "__main__":
    main()

