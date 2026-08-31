import pandas as pd
import os

csv = 'clean_final_data.csv'

def graphChoose():

    os.system('clear')
    print('[1] - Plot\n[2] - Scatter\n[3] - Bar\n[4] - Stemn\n[5] - Fill Between\n[6] - Stackplot')

    chooseGraph_User = input("Choose wich graphic do you want to display the info: ")

    if chooseGraph_User == '1':
        os.system('clear')
        print('You choose the Plot graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '2':
        os.system('clear')
        print('You choose the Scatter graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '3':
        os.system('clear')
        print('You choose the Bar graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '4':
            os.system('clear')
            print('You choose the Stemn graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '5':
            os.system('clear')
            print('You choose the Fill Between graph and want to show just', chooseUser, '\n')

    elif chooseGraph_User == '6':
            os.system('clear')
            print('You choose the Stackplot graph and want to show just', chooseUser, '\n')
    return 0

os.system('clear')
print("\n[1] - Order Date\n[2] - Quantity\n[3] - Product Name\n[4] - Unit Price\n[5] - City\n[6] - Age")

chooseUser = input("\nChoose wich column you want to see: ")

if chooseUser == '1':
    df = pd.read_csv(csv, usecols=[
        "ProductName",
        "OrderDate"], nrows=20)

    chooseUser = "Oder Date"

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

    chooseUser = "Product Name"


    os.system('clear')
    print('\n', df,'\n')

elif chooseUser == '4':
    df = pd.read_csv(csv, usecols=[
        "ProductName",
        "UniPrice",
    ], nrows=20)

    chooseUser = "Unit Price"

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