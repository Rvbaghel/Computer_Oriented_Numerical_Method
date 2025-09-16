# Function to generate divided difference table
import math
def forwordtabel(x, y):
    n = len(x)
    
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    
   
    for i in range(n):
        table[i][0] = y[i]
    
 
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1])
    
    return table

def forword_interpolation(x, y, value):
    n = len(x)
    table = forwordtabel(x, y)
    result = table[0][0]
    h=x[1]-x[0]
    term = 1
    for i in range(1, n):
        term *= (value - x[i-1])
        tem=(term*table[0][i])/(math.factorial(i)*(h**i))
        result += tem
    return result, table

# Given values
x_points = [0, 0.1, 0.2 ,0.3 ,0.4]
y_points = [1.0000 ,1.1052, 1.2214 ,1.3499, 1.4918]
x_to_find = 0.38

value, table =  forword_interpolation(x_points, y_points, x_to_find)

print("Divided Difference forword Table:")
for row in table:
    print(row)
print(f"\nValue at f({x_to_find}) = {value:.4f}")
