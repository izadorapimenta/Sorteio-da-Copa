""" O código cria um sorteio de chave de grupo para uma Copa, com quatro países na chave """

import random
RandNum = random.randint(1,24)

if RandNum > 0 and RandNum <=6:
    Pais = "Brazil"
if RandNum > 6 and RandNum <=12:
    Pais = "Germany"
if RandNum > 12 and RandNum <= 18:
    Pais = "Italy"
if RandNum > 18 and RandNum <=24:
    Pais = "Argentina"
print(("The first country is ") + Pais)
   
RandNum2 = random.randint(1,24)   
 
if RandNum2 > 0 and RandNum2 <=6:
    Pais2 = "Brazil"
if RandNum2 > 6 and RandNum2 <=12:
    Pais2 = "Germany"
if RandNum2 > 12 and RandNum2 <= 18:
    Pais2 = "Italy"
if RandNum2 > 18 and RandNum2 <= 24:
    Pais2 = "Argentina"
print (("The second country is ") + Pais2)

RandNum3 = random.randint (1,24)

if RandNum3 > 0 and RandNum3 <=6:
     Pais3 = "Brazil"
if RandNum3 > 6 and RandNum3 <=12:
     Pais3 = "Germany"
if RandNum3 > 12 and RandNum3 <=18:
     Pais3 = "Italy"
if RandNum3 > 18 and RandNum3 <=24:
     Pais3 = "Argentina"
print (("The third country is ") + Pais3)

    
if Pais == Pais2:
   print ("Try again!")
elif Pais2 == Pais3:
   print ("Not this time! Try again!")
elif Pais == Pais3:
   print ("No donut for you. Try again.")
else:
   print ("Yes! We've got the first group of the Cup!")

if Pais != Pais2 and Pais2 != Pais3 and Pais3 != Pais and Pais != "Argentina" and Pais2 != "Argentina" and Pais3 != "Argentina":
        print ("Argentina is the another country!")

if Pais != Pais2 and Pais2 != Pais3 and Pais3 != Pais and Pais != "Germany" and Pais2 != "Germany" and Pais3 != "Germany":
        print ("Germany is the another country!")

if Pais != Pais2 and Pais2 != Pais3 and Pais3 != Pais and Pais != "Italy" and Pais2 != "Italy" and Pais3 != "Italy":
        print ("Italy is the another country!")

if Pais != Pais2 and Pais2 != Pais3 and Pais3 != Pais and Pais != "Brazil" and Pais2 != "Brazil" and Pais3 != "Brazil":
        print ("Brazil is the another country!")

