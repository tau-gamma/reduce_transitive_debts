import numpy as np
import pandas as pd


def compute_everything(list_of_tuples, names):
    """
    list of tuples where a tuple contains (who paid, what amount, who owes the amount) 
    "who owes the amount" can also be 0 which means that amount gets divided by all persons inculding the one who paid
    """
    
    #find the amount of people that are in the list
    maximum = 0
    for (x,_,y) in list_of_tuples:
        maximum = max(maximum, x, y)
    matrix = np.zeros((maximum,maximum))

    #create the matrix of who owes whom how much
    for (x, amount, y) in list_of_tuples:
        if y == 0:
            matrix[:,x-1] += amount/maximum
        else:
            matrix[y-1, x-1] += amount


    print("\n\nWho (row) owes whom (column) how much \n")
    print(pd.DataFrame(data=matrix, columns=names, index=names), "\n")
    print("Who has consumed how much \n")
    print(pd.DataFrame(data=[matrix.sum(axis=1)], columns=names, index=["Amount"]), "\n")
    print("Who has to pay and who gets payed how much \n")
    print(pd.DataFrame(data=[reduce_matrix_to_vector(matrix)], columns=names, index=["Amount"]), "\n")


def reduce_matrix_to_vector(matrix):
    """ 
    Takes a payment matrix and reduces it to a vector by resolving all transitive debts 
    returns a vector where every entry represents the amount an individual owes to or receives from the collective
    """
    matrix -= matrix.T
    matrix = np.tril(matrix, 0)
    matrix[:,0] -= matrix.sum(axis=0)
    return matrix.sum(axis=1)


def convert_named_list_to_unnamed_list(l):
    dict = {}
    count = 0
    nl = []

    for (x, betrag, y) in l:
        number_name_x = 0
        if x in dict:
            number_name_x = dict[x]
        else:
            count +=1
            dict[x] = count
            number_name_x = count
        
        number_name_y = 0
        if y == "All":
            number_name_y = 0
        else:
            if y in dict:
                number_name_y = dict[y]
            else:
                count +=1
                dict[y] = count
                number_name_y = count
        nl.append((number_name_x, betrag, number_name_y))
    return dict, nl


def convert_excel_string_to_named_list(s):
    arr = []
    for row in filter(lambda i: i.strip() != "" and i != "\t\t\t", s.split("\n")):
        name, amount, _, debtor = row.split("\t")
        arr.append((name.strip(), float(amount.replace(",", ".").replace("€", "")), debtor.strip()))
    return arr



if __name__ == '__main__':
    pstring = """
        Mickey Mouse	123,00 €	Ice	Minnie Mouse
        Mickey Mouse	345,00 €	Hotel	Donald Duck
        Mickey Mouse	213,00 €	Restaurant	Daisy Duck
        Mickey Mouse	1,00 €	Car	Goofy
        Mickey Mouse	23,00 €	Car	Goofy
        Mickey Mouse	89,00 €	Hotel	Donald Duck
                    
        Minnie Mouse	1,00 €	Ice	Mickey Mouse
        Minnie Mouse	2,00 €	Hotel	Minnie Mouse
        Minnie Mouse	3,00 €	Restaurant	Donald Duck
        Minnie Mouse	4,00 €	Car	Daisy Duck
        Minnie Mouse	5,00 €	Car	Goofy
        Minnie Mouse	6,00 €	Hotel	Donald Duck
                    
        Donald Duck	1,00 €	Ice	Mickey Mouse
        Donald Duck	2,00 €	Hotel	Minnie Mouse
        Donald Duck	3,00 €	Restaurant	Donald Duck
        Donald Duck	4,00 €	Car	Daisy Duck
        Donald Duck	5,00 €	Car	Mickey Mouse
        Donald Duck	6,00 €	Hotel	Mickey Mouse
                    
        Daisy Duck	15,00 €	Taxi	Donald Duck
                    
        Goofy	51,00 €	Party	All
    """

    arr = convert_excel_string_to_named_list(pstring)
    names, unnamed_list = convert_named_list_to_unnamed_list(arr)
    compute_everything(unnamed_list, names.keys())