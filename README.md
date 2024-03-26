Solve square equation -----
```python3
print('hello system')
bad_data = True
while bad_data == True:
    try:
        a = int(input('enter a: '))
        b = int(input('enter b: '))
        bad_data = False
    except ValueError:
        print('error')
    except ZeroDivisionError:
        print('zero error')
    except:
        print('some error')

print(f'summ {a} and {b} = {a+b}')

```
