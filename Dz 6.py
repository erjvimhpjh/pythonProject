result = []

def divider(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            if b != 0:
                if a < b:
                    raise ValueError
                if b > 100:
                    raise IndexError
                return a / b
            else:
                raise ZeroDivisionError
        else:
            raise TypeError("Unsupported types for division.")
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")
    except IndexError as ie:
        print(f"Caught IndexError: {ie}")
    except TypeError as te:
        print(f"Caught TypeError: {te}")
    except ZeroDivisionError as zde:
        print(f"Caught ZeroDivisionError: {zde}")

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
