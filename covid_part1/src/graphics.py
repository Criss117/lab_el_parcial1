import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/data.csv')

def state():
  recovered = df[df['Recuperado'] == 'Recuperado'].shape[0]
  deceased = df[df['Recuperado'] == 'Fallecido'].shape[0]
  undefined = df['Recuperado'].isna().sum()

  states = ['Recuperado', 'Fallecido', 'No definido']
  amount = [recovered, deceased, undefined]

  for state, value in zip(states, amount):
    print(f"Número de {state}: {value}")
  print("Total:", recovered + deceased + undefined)

  data = {
    "hue": states,
    "y": amount,
    "xlabel": 'Estados',
    "ylabel": 'Número',
    "title": 'Cantidad de personas por estado'
  }

  show(data)

def gender():
  famale = df[df["Sexo"] == "F"].shape[0]
  male = df[df["Sexo"] == "M"].shape[0]

  print("Numero de mujeres:", famale)
  print("Numero de hombres:", male)
  print("Total:", famale + male)

  genders = ['F', 'M']
  amount = [famale, male]

  data = {
    "hue": genders,
    "y": amount,
    "xlabel": 'Generos',
    "ylabel": 'Número',
    "title": 'Cantidad de personas por género'
  }

  show(data)

def stateByGender():
  recoveredMen = df[(df['Sexo'] == 'M') & (df['Recuperado'] == 'Recuperado')].shape[0]
  recoveredWomen = df[(df['Sexo'] == 'F') & (df['Recuperado'] == 'Recuperado')].shape[0]
  deceasedMen = df[(df['Sexo'] == 'M') & (df['Recuperado'] == 'Fallecido')].shape[0]
  deceasedWomen = df[(df['Sexo'] == 'F') & (df['Recuperado'] == 'Fallecido')].shape[0]

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
  community = df[df['Tipo de contagio'] == 'Comunitaria'].shape[0]
  related = df[df['Tipo de contagio'] == 'Relacionado'].shape[0]

  print("Contagios de tipo comunitario", community)
  print("Contagios de tipo relacionado", related)
  print("Total:", community + related)

  sizes = [community, related]
  labels = ['Comunitario', 'Relacionado']

  # Crear el gráfico circular
  plt.figure(figsize=(6,6))
  plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
  plt.axis('equal') 
  plt.title('Tipo de contagio')

  # Mostrar el gráfico
  plt.show()

def show(data):
  sns.set_theme(style="whitegrid")

  sns.barplot(hue=data["hue"], y=data["y"])
  
  plt.xlabel(data["xlabel"])
  plt.ylabel(data["ylabel"])
  plt.title(data["title"])

  plt.show()