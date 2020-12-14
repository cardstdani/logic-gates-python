a = 0
b = 0

c = 0
d = 1

e = 1
f = 0

g = 1
h = 1

def NotGate(x):
  return (x+1)+(x+1)*-x

def AndGate(x, y):
  return x*y

def OrGate(x, y):
  return (x+y)-(x*y)

def NorGate(x, y):
  return (x*y)+1-(x+y)

def XorGate(x, y):
  return (x+y)-2*(x*y)

def XnorGate(x, y):
  return (x*y) + 0**(x+y)

#NOT GATE
print("NOT gate:\n")
print(NotGate(a))
print(NotGate(d))

#AND GATE
print("AND gate:\n")
print(AndGate(a, b))
print(AndGate(c, d))
print(AndGate(e, f))
print(AndGate(g, h))

#OR GATE
print("OR gate:\n")
print(OrGate(a, b))
print(OrGate(c, d))
print(OrGate(e, f))
print(OrGate(g, h))

#NOR GATE
print("NOR gate:\n")
print(NorGate(a, b))
print(NorGate(c, d))
print(NorGate(e, f))
print(NorGate(g, h))

#XOR GATE
print("XOR gate:\n")
print(XorGate(a, b))
print(XorGate(c, d))
print(XorGate(e, f))
print(XorGate(g, h))

#XNOR GATE
print("XNOR gate:\n")
print(XnorGate(a, b))
print(XnorGate(c, d))
print(XnorGate(e, f))
print(XnorGate(g, h))
