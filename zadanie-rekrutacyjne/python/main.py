# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu

import os
from json import load

#Get the current directory of the script
current_dir = os.path.dirname(__file__)

#Build the path to the "kategorie.json" and "zbiór_wejściowy.json" file
filepath_category = os.path.join(current_dir, '..', 'dane', 'kategorie.json')
filepath_set = os.path.join(current_dir, '..', 'dane', 'zbiór_wejściowy.json')

#Load files
with open(filepath_category, 'r', encoding='utf-8') as category_file:
    data_category = load(category_file)


with open(filepath_set, 'r', encoding='utf-8') as set_file:
    data_set = load(set_file)


#Function for changing unit to oz
def unit_change(element):
    if element[-2:].isalpha(): 
        unit = element[-2:] 
        value_str = element[:-2] 
    else:
        unit = element[-1]  
        value_str = element[:-1]  
    
    value = float(value_str.replace(',','.'))

    if unit == "ct":
        return value * 0.0070548
    elif unit == "g":
        return value * 0.035274
    
#function for calculate the value
def calculate_value():
    for n in range(len(data_set)):
        weight = unit_change(data_set[n]['Masa'])
        for i in range(len(data_category)):
            if (data_set[n]['Typ'] == data_category[i]['Typ']) and (data_set[n]['Czystość'] == data_category[i]['Czystość']):
                value = weight * data_category[i]['Wartość za uncję (USD)']
                values.append({"wartość":value, "id":n})

#Function call
values = []        
calculate_value()
values_sorted = sorted(values, key=lambda x: x['wartość'], reverse=True)

#Print out top 5 values datas
print("\n5 o największej wartości na jednostkę:\n")
for i in range(0, 5, 1):
    data = data_set[values_sorted[i]['id']]
    print(f"Typ: {data['Typ']}\nMasa: {data['Masa']}\nCzystość: {data['Czystość']}\nBarwa: {data['Barwa']}\nPochodzenie: {data['Pochodzenie']}\nWłaściciel: {data['Właściciel']}\nWartość (USD): {values_sorted[i]['wartość']}\n\n")
    