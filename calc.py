import os
flag = False 

print("Instrukcja: ")    
print("Najpierw podaj pierwszą liczbę\nnastępnie wybierz instrukcję \na na koniec drugą liczbę")
print("Aby zakończyć wpisz \"end\"")

while flag == False:
    first = input("Pierwsza wartość: ")
    if(first == "end"):
        print("Kalkulator wyłączony") 
        exit()
    else:
        first = int(first)


    print("Dodawnie    - a")
    print("Odejmowanie - s")
    print("Mnozenie    - m")
    print("Dzielenie   - d")
    print("Koniec      - end")
    dzialanie = input("Wybierz działanie: ")
    if(dzialanie == "end"):
        print("Kalkulator wyłączony") 
        exit() 

    second = input("Druga wartość: ")
    if(second == "end"):
        print("Kalkulator wyłączony")
        exit()
    else:
        second = int(second)

    print("Wynik: ", end="")
    if(dzialanie == "a"):
        print(first + second)
    if(dzialanie == "s"):
        print(first - second)
    if(dzialanie == "m"):
        print(first * second)
    if(dzialanie == "d"):
        print(first // second)
    

    print("\n")

    




