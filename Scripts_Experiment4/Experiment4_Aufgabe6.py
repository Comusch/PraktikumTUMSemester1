import Analysistools as an
import math
import numpy

print("--------------Load Data-----------")

(245, 35.5)
#Vorerst
p_k = 35.5 # bar
V_k = 245*10**(-6) # m^3/mol
Na = 6.02214*10**23

print(f"p_k:{p_k}")
print(f"V_k:{V_k}")

print("--------Calculation for mol----------")
b = V_k /3
a = p_k * 10**5 * 27 *b**2
print(f"b:{b}")
print(f"a:{a}")

print("--------Calculation of the uncertanty--------")
u_b = 0.000002
u_p = 2
u_a = math.sqrt(((27*b**2)*u_p)**2+(27*p_k*10**5*2*b*u_b)**2)
print(f"u_b: {u_b}")
print(f"u_p: {u_p}")
print(f"Fehlerfortpflanzung: u_a: {u_a}")

print("--------Calculation for partical")

b_p = b*Na
a_p = p_k*10**5 * 27 *b_p**2

print(f"b_p:{b_p}")
print(f"a_p:{a_p}")


