from math import sqrt

print("hello solving system")
bad_data = True
while bad_data == True:
    try:
        a = int(input('enter a: '))
        b = int(input('enter b: '))
        c = int(input('enter c: '))
        bad_data = False
    except ValueError:
        print('error')
    except ZeroDivisionError:
        print('zero error')
    except:
        print('some error')

D = b*b - (4*a*c)
print(f'value = {D}')

if D > 0:
    d = sqrt(D)
    X1 = ((-b) + d)/(2*a)
    X2 = ((-b) - d)/(2 * a)
    print(f'1 root = {X1}, 2 root = {X2}')
elif D == 0:
    X1 = (-b)/(2*a)
    print(f'1 root = {X1}')
else:
    print('no roots')