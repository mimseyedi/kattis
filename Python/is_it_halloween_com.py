line = input()
month, day = line.split()

if month == 'OCT' and day == '31':
    print('yup')
elif month == 'DEC' and day == '25':
    print('yup')
else:
    print('nope')
