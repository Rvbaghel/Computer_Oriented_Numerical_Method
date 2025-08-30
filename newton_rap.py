#remeber that one time we do derivative only statment
#any root derivative 2x remeber 
def f_x(value):
    return value**2 - 2

# def f_x(value):
#     return value**3 - (4*value) - 9

# def derivatives(value):
#     return 3 * pow(value,2) -4 
    
def derivatives(value):
    return 2 *value 
    
def newton_raphson(x0,tol):
    
    
    print(f"{'Iter':<5} {'x0':<10} {'f(x0)':<12}  {'f(x1)_d':<12} {'c':<10}  {'Error':<10}")
    print("-"*80)       

    iteration=1
    error=0
    old_value=0
    while True:
        
        f_x0=f_x(x0)
        f_x_d=derivatives(x0)
        
        if f_x_d == 0:
            print("Derivative became zero. Stopping.")
            break

        c=x0-(f_x0/f_x_d)
        
        error=abs(c-old_value)
        print(f"{iteration:<5} {x0:<10.6f} {f_x0:<12.6f} {f_x_d:<12.6f} {c:<10.6f}  {round(error,4):<10}")
        
        if error < tol :
            print("Root Is :",round(c,4))
            break
            
        x0=c
        old_value=c
        iteration+=1
       
x0=1
tol=0.00001    
newton_raphson(x0,tol)