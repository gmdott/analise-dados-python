# Neste código eu estou estudando a leitura dos dados do csv com  o pandas
# e externando dos dados em forma de gráfico com a lib matplot

import pandas as pd
import matplotlib.pyplot as plt




csv = 'clean_final_data.csv'

df = pd.read_csv(csv, usecols=[
    "ProductName",
    "Quantity"
], nrows=20)
df["Quantity"] = df["Quantity"].astype(int)

df.plot(
    x = "ProductName",
    y = "Quantity",
    kind = "bar",
    title = "Quantitade por Produto",
    xlabel = "Produto",
    ylabel = "Quantidade",
    figsize = (10, 6),
    color = "steelblue",
    legend = False   
)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
