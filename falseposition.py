def f(value):
    return value**3 - (4*value) -9 


def falsePositionMethod(a,b,tol):
    if f(a) * f(b) >=0:
         return 
    
    print(f"{'Iter':<5} {'a':<10} {'f(a)':<12} {'b':<10} {'f(b)':<12} {'c':<10} {'f(c)':<12} {'Error':<10}")
    print("-"*80)       

    iteration=1
    c_old=a
    while True:
        f_a=f(a)
        f_b=f(b)
       
        #remeber this one i reduce some posions 
        a_f=a*f_b
        b_f=b*f_a
        
        #remeber
        dvi=f_b-f_a
        
        # remeber 
        c=(a_f-b_f)/dvi
       
        f_c=f(c)
        
        errors=0
        error=abs(c-c_old)
        
        if iteration > 1:
            errors=error
        
        print(f"{iteration:<5} {a:<10.6f} {f_a:<12.6f} {b:<10.6f} {f_b:<12.6f} {c:<10.6f} {f_c:<12.6f} {round(errors,4):<10}")
        
        if f_c == 0 or error < tol:
            print(f"Root Is Found {round(c,4)}")
            break
        
        if f_a * f_c < 0:
            b = c
        else:
            a = c     
        
        c_old=c
        iteration+=1
        
         


a=2
b=3
tol=0.01

falsePositionMethod(a,b,tol)

