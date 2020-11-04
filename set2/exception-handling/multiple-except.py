try:
    x, y = [int(x) for x in input().split()]
    c = x / y
    print("c : ", c)
except ZeroDivisionError:
    print("ZeroDivisionError, Can't divide with Zero")
# except ValueError:
#     print("Give integer values only")
except:
    print("Default Except: Please provide valid input only")
