import math

# Function to generate backward difference table
def backward_table(x, y):
    n = len(x)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = y[i]
    
    # Fill backward difference table
    for j in range(1, n):
        for i in range(j, n):
            table[i][j] = table[i][j-1] - table[i-1][j-1]
    
    return table

def backward_interpolation(x, y, value):
    n = len(x)
    table = backward_table(x, y)
    result = table[n-1][0]   # Start from last value
    h = x[1] - x[0]
    term = 1
    
    for i in range(1, n):
        term *= (value - x[n-i])   # (x - xn)(x - xn-1)...
        temp = (term * table[n-1][i]) / (math.factorial(i) * (h ** i))
        result += temp
    
    return result, table

# Example usage
x_points = [0, 0.1, 0.2, 0.3, 0.4]
y_points = [1.0000, 1.1052, 1.2214, 1.3499, 1.4918]
x_to_find = 0.38

value, table = backward_interpolation(x_points, y_points, x_to_find)

print("Backward Difference Table:")
for row in table:
    print(row)
print(f"\nValue at f({x_to_find}) = {value:.4f}")
