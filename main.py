import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template, request, send_file
import io

csv = 'clean_final_data.csv'

# Utiliza o flask para abrir um servidor (local) na web usando o template do 'index.html' e
# instancia rota para exibir um grafico com os dados que estão dentro do csv com o metodo POST
# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/grafico", methods=["POST"])
# def grafico():
#     arquivo = request.files["csv"]



def graphChoose():

    os.system('clear')
    print('[1] - Line\n[2] - Bar\n[3] - Horizontal Bar\n[4] - Pizza \n[5] - Histogram')

    chooseGraph_User = input("Choose wich graphic do you want to display the info: ")

    if chooseGraph_User == '1':
        os.system('clear')
        chooseGraph_User = "line"

        #Inicia a leitura do csv com pandas
        df = pd.read_csv(csv, usecols=[
            "ProductName",
            chooseUser], nrows=50)
        df[chooseUser] = pd.to_datetime(df[chooseUser])
        #Realiza o grafico escolhido pelo usuário (plot) com o matplotlib
        df.plot(
            x = "ProductName",
            y = chooseUser,
            kind = "bar",
            title = "Data de compra do pedido",
            xlabel = "Produto",
            ylabel = "Data do pedido",
            figsize = (14, 6),
            color = "steelblue",
            #legend = False  
        )
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        #print('You choose the Plot graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '2':
        os.system('clear')
        chooseGraph_User = "bar"
        print('You choose the Scatter graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '3':
        os.system('clear')
        chooseGraph_User = "barh"
        print('You choose the Bar graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '4':
            os.system('clear')
            chooseGraph_User = "pie"
            print('You choose the Stemn graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '5':
            os.system('clear')
            chooseGraph_User = "hist"
            print('You choose the Fill Between graph and want to show just', chooseUser, '\n')
    return 0

os.system('clear')
print("\n[1] - Order Date\n[2] - Quantity\n[3] - Product Name\n[4] - Unit Price\n[5] - City\n[6] - Age")

chooseUser = input("\nChoose wich column you want to see: ")

if chooseUser == '1':
    #df = pd.read_csv(csv, usecols=[
    #    "ProductName",
    #    "OrderDate"], nrows=20)

    chooseUser = "OrderDate"

    #os.system está obsoleto, ele está sendo utilizado apenas como exemplo
    os.system('clear')
    graphChoose()
    #print('\n', df,'\n')

elif chooseUser == '2':
    df = pd.read_csv(csv, usecols=[
        "ProductName", 
        "Quantity"], nrows=20)
    #Transforma o os valores de quantity que estão em float, em int e também verifica se tem valor NaN
    df["Quantity"] = df["Quantity"].fillna(0).astype(int)

    chooseUser = "Quantity"

    os.system('clear')
    graphChoose()
    #print('\n', df,'\n')

elif chooseUser == '3':
    df = pd.read_csv(csv, usecols=[
        "ProductName"
    ], nrows=20)

    chooseUser = "ProductName"


    os.system('clear')
    print('\n', df,'\n')

elif chooseUser == '4':
    df = pd.read_csv(csv, usecols=[
        "ProductName",
        "UniPrice",
    ], nrows=20)

    chooseUser = "UnitPrice"

    os.system('clear')
    graphChoose()
    #print('\n', df,'\n')

elif chooseUser == '5':
    df = pd.read_csv(csv, usecols=[
        "ProductName",
        "City"  
    ], nrows=20)

    chooseUser = "City"

    os.system('clear')
    graphChoose()
    #print('\n', df,'\n')

elif chooseUser == '6':
    df = pd. read_csv(csv, usecols= [
        "ProductName",
        "Age"
    ], nrows=20)

    chooseUser = "Age"

    os.system('clear')
    graphChoose()
    #print('\n', df,'\n')
