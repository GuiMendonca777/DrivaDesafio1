#Gui Mendonça

#imports
import pandas as pd 

pd.set_option('display.max_rows',10,"display.max_columns",5)


#ler arquivo
df = pd.read_csv(".\DadosEmpresa.csv")
#print de colunas 
print("Colunas do arquivo: ")
print(df.columns.values)

#print primeiras linhas do arquivo
print("Primeiras linhas do arquivo:")
print(df.head())

#print empresas que tem a coluna opcao_pelo_simples com valor "SIM"
print("total de Colunas opcao_pelo_simples com valor sim: ")
#operação de comparação, depois pegando apenas uma coluna, no caso "cnpj" para mostrar
#apenas o valor numérico 
print(df[df["opcao_pelo_simples"]=="SIM"].count()["cnpj"])

#print soma do capital_social de todas as empresas
print("soma do capital_social de todas as empresas")
print(df["capital_social"].sum())

#print todas as empresas que tem "capital_social" maior que 10.000 e menor que 20.000;
print("capital_social entre 10000 e 20000: ")
#para aparecer todas as empresas :
pd.set_option('display.max_rows',len(df.index))
print(df[(df["capital_social"]>=10000) & (df["capital_social"] <=20000)].all)
#para não poluir a tela nos próximos prints 
pd.set_option('display.max_rows',10)

#lendo o arquivo dados endereco
df2 = pd.read_csv(".\DadosEndereco.csv")
#dando merge nos dois data_frames
df_merged = pd.merge(df,df2,on="cnpj")
#pegando apenas os dados que possuem valor CURITIBA como municipio
df_merged[df_merged["municipio"]=="CURITBA"].to_csv("DadosDeCuritiba.csv")


