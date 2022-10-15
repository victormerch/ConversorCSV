from time import sleep
import pandas as pd
class LectorCSV:
    def __init__(self, fichero):
        self.fichero = fichero
        
        self.df = self.filtrar(pd.read_csv(fichero))
        
    
    def getColumns(self):
        # print(self.df.columns.to_list())
        return self.df.columns.to_list()
    
    def getcolumsTypes(self):
        # print(self.df.dtypes.to_list())
        lista = self.df.dtypes.to_list()
        listaTipos = []
        for tipo in lista:
            if tipo == "int64":
                listaTipos.append("BIGINT")
            elif tipo == "O":
                listaTipos.append("VARCHAR(100)")
            elif tipo == "float64":
                listaTipos.append("FLOAT")
        # print(listaTipos)
        return listaTipos
    
    def getRows(self):
        # print(self.df.to_dict('list'))
        return self.df.to_dict('list')
    
    def filtrar(self,df):
        df = df.dropna()
        df = df.drop_duplicates()
        return df
    