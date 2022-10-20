import mysql.connector
class SQLConector:
    
    def __init__(self):
       self = self
       

    def conexion(self,user,password,host,db):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        try:
            self.mydb = mysql.connector.connect(host=self.host,
                                                user=self.user,
                                                password=self.password,
                                                database=self.db)
                                        
            return True
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False
    
    def createTable(self,name,columsTypes,columns,datos):
        try:
            query1 = f"CREATE TABLE {name} ("
            for i in range(len(columns)):
                
                    
                query1 += f"{columns[i]} {columsTypes[i]}"
                if i == 0:
                    query1 += " PRIMARY KEY"
                if i != len(columns)-1:
                    query1 += ","
                else:
                    query1 += ");"
                    
            
            
            mycursor = self.mydb.cursor()
            mycursor.execute(query1)
            self.mydb.commit()
            print("===Tabla creada correctamente===")
            self.insertInTable(name,columns,columsTypes,datos)
            
            return True
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False  
        
    def insertInTable(self,name,columns,columsTypes,datos):
        try:
            query = f"insert into {name} values "
            for i in range (0,len(datos[columns[0]])):
                row = "("
                
                for y in range (0,len(columns)):
                    if columsTypes[y] == "VARCHAR(100)":
                        row += f"'{datos[columns[y]][i]}'"
                    else:
                        row += f"{datos[columns[y]][i]}"
                    if y != len(columns)-1:
                        row += ","
                query += row + ")"
                
                if i != len(datos[columns[0]])-1:
                    query += ","
                else:
                    query += ";"
            
            mycursor = self.mydb.cursor()    
            mycursor.execute(query)
            
            self.mydb.commit()
            
            return True
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False  