# Funktion, welche zwei Zahlen multipliziert und anschliessend addiert
def fmac(a, b, c):
    result = a * b + c
    return result

result_1 = fmac(1.0, 2.0, 3.0)
result_2 = fmac(4.0, 5.0, 6.0)
result_3 = fmac(7.0, 8.0, 9.0)
print(result_1, result_2, result_3)

# Funktionsaufruf mittels Parameter
a_caller = 1.0
b_caller = 2.0
c_caller = 3.0
result = fmac(a_caller, b_caller, c_caller)
print(result)

