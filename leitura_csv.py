import pandas as pd
import numpy as np

#Lendo arquivo CSV
file_path = '/dados.csv'
data = pd.read_csv(file_path, sep=';', engine='python', encoding='utf-8')

#Exibindo os dados lidos
print('Dados do arquivo CSV')
print(data)

#Imprindo mais informações sobre os dados
print(data.info())

#Imprimindo as primeiras 5 linhas
print("Primeiras 5 linhas:")
print(data.head(5))

#Imprimindo as últimas 5 linhas
print("\nÚltimas 5 linhas:")
print(data.tail(5))
print() # Deixando uma linha em branco

#Criando uma copia do arquivo csv original
data_copia = data.copy()

#Alterando os dados de data_copia

#Substituindo todos os valores nulos da coluna ‘Calories’ por 0;
data_copia['Calories'] = data_copia['Calories'].fillna(0)

#Verificando se a mudança acima foi aplicada com sucesso;
print("Imprimindo o conteudo da variável data_copy")
print(data_copia)

#Substituindo valores nulos na coluna 'Date' por '1900/01/01'
data_copia['Date'] = data_copia['Date'].fillna('1900/01/01')

#Verificando se a substituição foi realizada
print("\n Coluna data com dados alterados:")
print(data_copia['Date'])

#Substituindo '1900/01/01' por NaN na coluna 'Date'
data_copia['Date'] = data_copia['Date'].replace('1900/01/01', np.nan)
print("\n Substituindo de '1900/01/01' por NaN:")
print(data_copia['Date'])

#Substituindo o valor que não está no formato correto
data_copia['Date'] = data_copia['Date'].replace({"20201226": "2020/12/26"})

#Convertendo a coluna 'Date' para o formato datetime
data_copia['Date'] = pd.to_datetime(data_copia['Date'].str.replace("'", ""), format='%Y/%m/%d')
print("\n Valor da coluna Date com formato corrigido:")
print(data_copia['Date'])

#Removendo registros que possuem valores nulos na coluna 'Date'
data_copia = data_copia.dropna(subset=['Date'])

#Encerrando com impressão de resultados.
print("\n Verificando os dados do dataframe:")
print(data_copia)