import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./data/data.xlsx')

def state():
  filtro = df[df["Ubicación"].isin(["Fallecido", "Recuperado"])]
  conteo = filtro["Ubicación"].value_counts()

  for state, value in conteo.items():
    print(f"Número de {state}: {value}")
  print("Total:", conteo.sum())

  data = {
    "hue": conteo.index,
    "y": conteo.values,
    "xlabel": 'Estados',
    "ylabel": 'Número',
    "title": 'Cantidad de personas por estado'
  }

  show(data)

def gender():
  filtro = df[df['Sexo'].isin(['F', 'M'])]
  conteo = filtro['Sexo'].value_counts()

  for state, value in conteo.items():
    print(f"Número de {state}: {value}")
  print("Total:", conteo.sum())

  data = {
    "hue": conteo.index,
    "y": conteo.values,
    "xlabel": 'Generos',
    "ylabel": 'Número',
    "title": 'Cantidad de personas por género'
  }

  show(data)

def stateByGender():
  recoveredMen = df[(df['Sexo'] == 'M') & (df['Ubicación'] == 'Recuperado')].shape[0]
  recoveredWomen = df[(df['Sexo'] == 'F') & (df['Ubicación'] == 'Recuperado')].shape[0]
  deceasedMen = df[(df['Sexo'] == 'M') & (df['Ubicación'] == 'Fallecido')].shape[0]
  deceasedWomen = df[(df['Sexo'] == 'F') & (df['Ubicación'] == 'Fallecido')].shape[0]

  states = ['Mujeres Recuperadas', 'Mujeres Fallecidas', 'Hombres Recuperados', 'Hombres Fallecidos']
  amount = [recoveredWomen, deceasedWomen, recoveredMen, deceasedMen]

  for state, value in zip(states, amount):
    print(f"Número de {state}: {value}")
  print("Total:", recoveredMen + recoveredWomen + deceasedMen + deceasedWomen)

  data = {
    "hue": states,
    "y": amount,
    "xlabel": 'Generos',
    "ylabel": 'Número',
    "title": 'Número de personas por Genero'
  }

  show(data)


def circular():
  conteo = df["Tipo"].value_counts()

  for state, value in conteo.items():
    print(f"Número de {state}: {value}")
  print("Total:", conteo.sum())

  # Crear el gráfico circular
  plt.figure(figsize=(6,6))
  plt.pie(conteo.values, labels=conteo.index, autopct='%1.1f%%', startangle=140)
  plt.axis('equal') 
  plt.title('Tipo de contagio')

  # Mostrar el gráfico
  plt.show()

def byDepartment():
  filtro = df[df["Ubicación"].isin(["Fallecido", "Recuperado"])]
  conteo = filtro.groupby('Departamento').size().sort_values()

  for state, value in conteo.items():
    print(f"Número de {state}: {value}")
  print("Total:", conteo.sum())

  data = {
    "hue": conteo.index,
    "y": conteo.values,
    "xlabel": 'Departamentos',
    "ylabel": 'Número',
    "title": 'Número de personas por Departamento'
  }

  show(data)

def show(data):
  sns.set_theme(style="whitegrid")

  sns.barplot(hue=data["hue"], y=data["y"])
  
  plt.xlabel(data["xlabel"])
  plt.ylabel(data["ylabel"])
  plt.title(data["title"])

  plt.show()



  