import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

ingresoTotal = lambda x: sum(x.Precio)
print(f"La tienda 1 tiene ingreso total de {round(ingresoTotal(tienda))} $")
print(f"La tienda 2 tiene ingreso total de {round(ingresoTotal(tienda2))} $")
print(f"La tienda 3 tiene ingreso total de {round(ingresoTotal(tienda3))} $")
print(f"La tienda 4 tiene ingreso total de {round(ingresoTotal(tienda4))} $")


