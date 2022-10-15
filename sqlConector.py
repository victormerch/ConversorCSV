from re import L
import mysql.connector
class SQLConector:
    
    def __init__(self,user,password,host,db):
       
       self.user = user
       self.password = password
       self.host = host
       self.db = db

    def getConexion(self):
        try:
            self.mydb = mysql.connector.connect(host=self.host,
                                           user=self.user,
                                           password=self.password,
                                           database=self.db)
                                        
            return self.mydb
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False
    def createTable(self,name,columsTypes,columns,datos):
        
        
        
        query1 = f"CREATE TABLE {name} ({columns[0]} {columsTypes[0]} PRIMARY KEY,{columns[1]} {columsTypes[1]},{columns[2]} {columsTypes[2]}, {columns[3]} {columsTypes[3]},{columns[4]} {columsTypes[4]},{columns[5]} {columsTypes[5]},{columns[6]} {columsTypes[6]},{columns[7]} {columsTypes[7]},{columns[8]} {columsTypes[8]},{columns[9]} {columsTypes[9]},{columns[10]} {columsTypes[10]},{columns[11]} {columsTypes[11]})"
        query2 = f"insert into {name} values "
        for i in range (0,len(datos[columns[0]])):
            #falta la conversion de tipos de datos
            #['BIGINT', 'BIGINT', 'BIGINT', 'VARCHAR(100)', 'VARCHAR(100)', 'FLOAT', 'BIGINT', 'BIGINT', 'VARCHAR(100)', 'FLOAT', 'VARCHAR(100)', 'VARCHAR(100)']
           query2 +=  f"({datos[columns[0]][i]},{datos[columns[1]][i]},{datos[columns[2]][i]},'{datos[columns[3]][i]}', '{datos[columns[4]][i]}',{datos[columns[5]][i]},{datos[columns[6]][i]},{datos[columns[7]][i]},'{datos[columns[8]][i]}', {datos[columns[9]][i]},'{datos[columns[10]][i]}','{datos[columns[11]][i]}')"
           if i != len(datos[columns[0]])-1:
               query2 += ","
        
        mycursor = self.mydb.cursor()
        mycursor.execute(query1)
        
        
        mycursor.execute(query2)
        self.mydb.commit()
        
        
        return True
                            
       
       