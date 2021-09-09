import datetime
from datetime import *
from tkinter import *
from openpyxl import *

### W tym pliku zajmę się utworzeniem domyślengo pustego arkusza takiego jaki dostajemy od Szefa.

#Tworzymy skoroszyt(wokrbook)
wb = Workbook()

#Następnie aktywujemy pierwszy arkusz kaukulacyjny naszego skoroszytu
sheet = wb.active

data = date.today()
start = input("Podaj start pracy w formacie H:M")
stop = input("Podaj koniec pracy w formacie H:M")



sheet.append((data,start, stop))










