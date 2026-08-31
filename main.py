import pandas as pd
import os

csv = 'clean_final_data.csv'

print("\n[1] - Order Date\n[2] - Quantity\n[3] - Product Name\n[4] - Unit Price\n[5] - City\n[6] - Age")

chooseUser = input("\nChoose wich column you want to see: ")

if chooseUser == '1':
    df = pd.read_csv(csv, usecols=[
        "ProductName",
        "OrderDate"], nrows=20)

    #os.system está obsoleto, ele está sendo utilizado apenas como exemplo
    os.system('clear')
    print(df)

elif chooseUser == '2':
    df = pd.read_csv(csv, usecols=[
        "ProductName", 
        "Quantity"], nrows=20)
    #Transforma o os valores de quantity que estão em float, em int e também verifica se tem valor NaN
    df["Quantity"] = df["Quantity"].fillna(0).astype(int)

    os.system('clear')
    print(df)

elif chooseUser == '3':
    df = pd.read_csv(csv, usecols=[
        "ProductName"
    ], nrows=20)

    os.system('clear')
    print(df)