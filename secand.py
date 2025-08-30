def f_x(value):
    return value**3 - value - 1


def secand_method(x0,x1,tol):
    
    
    print(f"{'Iter':<5} {'x0':<10} {'f(x0)':<12} {'x1':<10} {'f(x1)':<12} {'x3':<10} {'f(x3)':<12} {'Error':<10}")
    print("-"*80)       

    iteration=1
    error=0
    old_3=0
    while True:
           f_x0=f_x(x0)
           
           f_x1=f_x(x1)
           
           #remeber this one 
           x3=x1-f_x1*(x1-x0)/(f_x1-f_x0)
           
           f_x3=f_x(x3)
           
           error=x3-old_3
           
           print(f"{iteration:<5} {x0:<10.6f} {f_x0:<12.6f} {x1:<10.6f} {f_x1:<12.6f} {x3:<10.6f} {f_x3:<12.6f} {round(error,4):<10}")
            
           if error < tol :
               print("Root Is :",round(x3,4))
               break 
           
           x0,x1=x1,x3
           old_3=x3
           iteration+=1
                
                 
x0=1
x1=1.5
tol=0.001
secand_method(x0,x1,tol)