def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except:
        return False