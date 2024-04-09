# Reduce a transitive debt matrix to a single payment per entity

Given a group of people where everyone can pay for things for everyone else:
This code computes a final payment for each person such that all debts can be resolved. 

Example:

Given a list such as this one where everyone paid for something for someone else: 
Structure: (Creditor, Amount, Description [optional], Debtor)

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

The program computes the following:

    Who (row) owes whom (column) how much:
    
                  Mickey Mouse  Minnie Mouse  Donald Duck  Daisy Duck  Goofy 
    Mickey Mouse           0.0           1.0         12.0         0.0   10.2 
    Minnie Mouse         123.0           2.0          2.0         0.0   10.2 
    Donald Duck          434.0           9.0          3.0        15.0   10.2
    Daisy Duck           213.0           4.0          4.0         0.0   10.2
    Goofy                 24.0           5.0          0.0         0.0   10.2
    
    Who has consumed how much
    
            Mickey Mouse  Minnie Mouse  Donald Duck  Daisy Duck  Goofy
    Amount          23.2         137.2        471.2       231.2   39.2
    
    Who has to pay and who gets payed how much
    
            Mickey Mouse  Minnie Mouse  Donald Duck  Daisy Duck  Goofy
    Amount        -770.8         116.2        450.2       216.2  -11.8
