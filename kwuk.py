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

print(a+b)