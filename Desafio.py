import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

dadosConexao = ("Driver={SQL Server};"
                "Server=DESKTOP-QS7OHFD;"
                "Database=ContosoRetailDW")

conexao = pyodbc.connect(dadosConexao)
print("Conexão bem sucedida")

vendas = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.FactSales',conexao)

# print(vendas['DateKey'].max())
# print(vendas['DateKey'].min())

vendas['Lucro'] = vendas['SalesAmount'] - vendas['TotalCost'] - vendas['DiscountAmount']
vendasDiarias = vendas.groupby(['DateKey']).sum()
grafico = vendasDiarias['Lucro'].plot(figsize=(15, 5))
grafico.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
plt.show()

#print(vendasDiarias)