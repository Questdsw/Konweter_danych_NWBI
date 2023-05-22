import os
import json
import xmltodict

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

    if exit == 1 and os.path.exists(plik) == True :
        pass
    elif exit ==7:
        print("zakonczyłes program")
    else:
        print("wybrałeś złe rozszerzenie ")

        
        
