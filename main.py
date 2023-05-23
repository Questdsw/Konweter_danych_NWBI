import os
import json
import xmltodict
import yaml

exit = 0
while exit != 7:
    print("""
    1 - konwersje json na xml
    2 - konwersje json na yaml
    3 - konwersja xml na json
    4 - konwersja xml na yaml
    5 - konwersja yaml na json
    6 - konwersja yaml na xml
    7 - zakonczenie programu
    """)
    exit = int(input("Wybierz opcje: "))
    plik =input("Podaj nazwe pliku: ")
    plik2 = input("Podaj nazwe nowego pliku z roszerzeniem:")


    if exit == 1 and os.path.exists(plik) == True :
        file = open(plik, "r")
        python_dict = json.load(file)
        xml_file = open(plik2, "w")
        xmltodict.unparse(python_dict, output=xml_file)
        xml_file.close()
    elif exit == 2 and os.path.exists(plik) == True :
        file = open(plik,"r")
        python_dict = json.load(file)
        yaml_file = yaml.dump(python_dict)
        file1 = open(plik2, "w")
        yaml.dump(python_dict, file1)
        file1.close()
    elif exit == 3 and os.path.exists(plik) == True:
        xml_file = open(plik,"r")
        xml = xml_file.read()
        python_dict = xmltodict.parse(xml)
        file = open(plik2, "w")
        json.dump(python_dict, file)
        file.close()
        
    elif exit ==7:
        print("zakonczyłes program")
    else:
        print("wybrałeś złe rozszerzenie ")
