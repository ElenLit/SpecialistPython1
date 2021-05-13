# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

summa = 0
with open("info.txt", "r") as f:
    for line in f:
        line = line.rstrip('\r\n')
        try:
            line = int(line)
            summa += line
        except ValueError:
            pass

print(f'Сумма всех чисел равна {summa}')
