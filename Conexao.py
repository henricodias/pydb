import pyodbc
import pandas as pd

dadosConexao = ("Driver={SQL Server};"
                "Server=DESKTOP-QS7OHFD;"
                "Database=ContosoRetailDW")

conexao = pyodbc.connect(dadosConexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()

produtosDF = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.DimProduct', conexao)
print(produtosDF)