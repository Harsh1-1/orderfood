#!/usr/bin/env python3

import re
from porter2stemmer import Porter2Stemmer
bazzled_menu = "GOOD Afternoon - 07/10/2019 Lunch Starts From 1.00 PM\n                                             VEG & NON VEG--- MENU\nVEG LUNCH MENU = 35/-\n\n*Tandoori Salad, Bendi Kurkure , Palak Paneer , Steam Rice, Dal Makhani , Chapati & Papad, Rasgula*\n\nVEG COMBO LUNCH  = 35/- \n\n* Veg Fried Rice with Gravy & sweet**paneer Ghassi with Neer Dosa  & Sweet*\n\nNON VEG LUNCH MENU = 45/-\n\n*Tandoori Salad, Bendi Kurkure , Chicken Tikka Masala , Steam Rice, Dal Makhani , Chapati & Papad, Rasgula*\n\nNON VEG COMBO LUNCH = 45/-\n\n* Chicken Fried Rice with Gravy & sweet**Chicken Sukha with Neer Dosa  & sweet**\n\nHEALTH MEAL MENU \n\n*Mix Veg  soup = 15/**Rajma Mix Salad = 20/-,**Lemon Exotic  salad =20/,**Veg Pasta = 40/,**veg Broun Rice=35/\n\nNon Veg Health Meal:-\n \n*Roasted Chicken with Soup/Salad(Any one) = 35/-,**Roasted Chicken with Soup & Salad = 45/-,*\nChicken BBQ with Soup & Salad = 45/-,**Chicken pasta =45/,**Chicken brown rice =45/*"

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#function to get the list of all terms from one doc
def stringtoterms(string, stemming=False):

    #for refining input content
    delimiters = ".","(c)","?","-","#","*","_","/","(",")","!","'",'"',";",":","&","<",">","\r","\n","\t"
    regexPattern = '|'.join(map(re.escape, delimiters))
    refinedlist = re.split(regexPattern, string)

    termlist = []

    for word in refinedlist:
        if stemming == True:
            word = stemmer.stem(word)
        termlist.append(word)

    termlist = filter(None,termlist)
    #print termlist
    return list(termlist)

menu = stringtoterms(bazzled_menu)
for i in range(0, len(menu)):
    if "   " not in menu[i] and not hasNumbers(menu[i]) and not any(badword in menu[i].lower() for badword in ["menu", "veg","good", "any", "one"]) and len(menu[i]) >2:
        print(menu[i])