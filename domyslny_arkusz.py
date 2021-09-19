from datetime import *
from openpyxl import *

def days_cur_month():
    """Listing all days in curent month"""
    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    list_days = [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]
    return list_days


def blank_sheet_create(name='Adam Wawrzyniak'):
    """Creating a blank sheet with default text and making a good looking
    dimensions of columns"""
    wb = Workbook()
    sheet = wb.active
    sheet["A1"] = name
    sheet.column_dimensions['A'].width = 12
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 10
    sheet.column_dimensions['E'].width = 18
    sheet.merge_cells('A1:B1')
    sheet.merge_cells('B2:C2')
    sheet["A2"] = datetime.today().strftime("%m-%y")
    sheet["B2"] = 'suma godzin'
    sheet["E2"] = 'Uwagi/lokalizacja'
    """There we list all month dates in rows"""
    days_cur_month()
    n = 3
    for day in days_cur_month():
        sheet.cell(row=n, column=1).value = day
        n += 1
    file = wb.save("new_file.xlsx")
    """"""
    return file

### To co mamy poniżej musi znajdować się w oddzielnym pliku.
## W tym pliku niech zostaną tylko funkcję.

start_prompt = "Witaj w aplikacji do zapisywania i obliczania czasu pracy.\n" \
               "Wybierz\n\t1-Aby utworzyć nowy arkusz.\n\t2-Aby edytować " \
               "istniejący."


print(start_prompt)

chose = int(input(':'))

if chose == 1:
    #name = input("Podaj swoje imie i nazwisko")
    blank_sheet_create()

# Dalej ustawić poszerzenia pól w arkuszu
# Ogarnąc sposób na robienbie sumy, automatycznie od ilości dni w miesiącu.
# Dodać kolorki w miejscach weekendów




