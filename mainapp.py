from domyslny_arkusz import blank_sheet_create

start_prompt = "Witaj w aplikacji do zapisywania i obliczania czasu pracy.\n" \
               "Wybierz\n\t1-Aby utworzyć nowy arkusz.\n\t2-Aby edytować " \
               "istniejący."


print(start_prompt)

chose = int(input(':'))

if chose == 1:
    blank_sheet_create()
