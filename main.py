"""
======TAREAS======
- [ ] Implementar try and catch para los posibles errores
- [ ] Implementar metodos para que no pare el programa si hay un error
- [ ] Comentar codigo
==================
"""

import mysql.connector
from lectorCSV import LectorCSV
from sqlConector import SQLConector

def main():
    lcsv = LectorCSV("titanic.csv")
    sql = SQLConector("root","test","localhost","IABD")
    conexion = sql.getConexion()
    if conexion != False:
        print("Base de datos conectada...")
        print("Procesando informacion del csv...")
        columnas = lcsv.getColumns()
        typeColumns = lcsv.getcolumsTypes()
        datos = lcsv.getRows()
        print("Insertando datos en la base de datos...")
        
        name = input("Que nombre quieres darle a la tabla? ")
        if sql.createTable(name,typeColumns,columnas,datos):
            print("Datos insertados correctamente")
        
    else:
        print("Error en la conexion")
    

if __name__ == "__main__":
    main()

