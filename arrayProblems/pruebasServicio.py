import pandas as pd

df = pd.read_csv("camaraDiputados.csv")

#print("DF en genereal \n")
#print(df, "\n")

#print("Df unicamente con hombres \n")
#print(df["Sexo"].value_counts()['Hombres'])

SexoYTotal = df[["Partido","Sexo", "Total"]]
SexoYTotalA = SexoYTotal.set_index("Partido")

#print(SexoYTotalA)

#print("Total de mujeres \n")
#print(SexoYTotalA)

'''df_mujeres = SexoYTotalA[SexoYTotalA['Sexo'] == 'Mujeres'][['Sexo', 'Total']]
print(df_mujeres['Total'].sum())'''

df_anio = pd.read_csv("CorrecionDatos.xlsx - Data.csv")
print(df_anio)

df= df_anio.set_index("Country Name")
print(df)