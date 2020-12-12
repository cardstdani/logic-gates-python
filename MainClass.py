a = 0
b = 1

#NOT GATE
print("NOT gate with A variable:\n")
print((a+1)+(a+1)*-a)

#AND GATE
print("AND gate with both variables:\n")
print(a*b)

#OR GATE
print("OR gate with both variables:\n")
print((a+b)-(a*b))

#NOR GATE
print("NOR gate with both variables:\n")
print((a*b)+1-(a+b))

#XOR GATE
print("XOR gate with both variables:\n")
print(-1*(a**b - 1))

#XNOR GATE
print("XNOR gate with both variables:\n")
print((a*b) + 0**(a+b))
