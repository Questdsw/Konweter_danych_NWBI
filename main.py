import os
import json
import xmltodict
import yaml
from yaml import SafeLoader
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
    while True:
        try:
            exit = int(input("Wybierz opcje: "))
            break
        except ValueError:
            print("!błędny wybór! Wpisz liczbe od 1-7")
    plik =input("Podaj nazwe pliku: ")
    plik2 = input("Podaj nazwe nowego pliku z roszerzeniem:")

    if exit == 1 and os.path.exists(plik) == True and str(plik[-4:])=="json":
        file = open(plik, "r")
        python_dict = json.load(file)
        xml_file = open(plik2, "w")
        xmltodict.unparse(python_dict, output=xml_file)
        xml_file.close()
    elif exit == 2 and os.path.exists(plik) == True and str(plik[-4:])=="json":
        file = open(plik,"r")
        python_dict = json.load(file)
        yaml_file = yaml.dump(python_dict)
        file1 = open(plik2, "w")
        yaml.dump(python_dict, file1)
        file1.close()
    elif exit == 3 and os.path.exists(plik) == True and str(plik[-4:])=="xml":
        xml_file = open(plik,"r")
        xml = xml_file.read()
        python_dict = xmltodict.parse(xml)
        file = open(plik2, "w")
        json.dump(python_dict, file)
        file.close()
    elif exit == 4 and os.path.exists(plik) == True and str(plik[-4:])=="xml":
        xml_file = open(plik, "r")
        xml_string = xml_file.read()
        python_dict = xmltodict.parse(xml_string)
        file = open(plik2, "w")
        yaml.dump(python_dict, file)
        file.close()
    elif exit == 5 and os.path.exists(plik) == True and str(plik[-4:])=="yaml":
        yaml_file = open(plik, "r")
        python_dict = yaml.load(yaml_file, Loader=SafeLoader)
        file = open(plik2, "w")
        json.dump(python_dict, file)
        file.close()
    elif exit == 6 and os.path.exists(plik) == True and str(plik[-4:])=="yaml":
        yaml_file = open(plik, "r")
        python_dict = yaml.load(yaml_file, Loader=SafeLoader)
        file = open(plik2, "w")
        xml_string = xmltodict.unparse(python_dict, output=file)
        file.close()
        yaml_file.close()

    elif exit ==7:
        print("zakonczyłes program")
    else:
        print("wybrałeś złe rozszerzenie, nazwe bądź opcje. Spróbuj jeszcze raz")
#
