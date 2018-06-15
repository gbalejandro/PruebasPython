# months = [
# 'January',
# 'February',
# 'March',
# 'April',
# 'May',
# 'June',
# 'July',
# 'August',
# 'September',
# 'October',
# 'November',
# 'December'
# ]

# endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
# + ['st', 'nd', 'rd'] + 7 * ['th'] \
# + ['st']
# year = input('Year: ')
# month = input('Month (1-12): ')
# day = input('Day (1-31): ')
# month_number = int(month)
# day_number = int(day)

# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]
# print(month_name + ' ' + ordinal + ', ' + year)

# def pedir_pizza():
#     print("Pedir Pizza".upper())

# pedir_pizza()

vocales = "aeiou"

for vocal in vocales:
    print(vocal.upper())

# try:
#     numero_1 = int(input("Dame un numero "))
#     numero_2 = int(input("Dame otro numero "))
# except ValueError:
#     print("Ese no es un numero")
# else:
#     total = numero_1 + numero_2
#     print("La suma es: "+ str(total))