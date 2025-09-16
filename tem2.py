# def f_xvalues(value):
#     return (value**4)-(value)-10

# def bisection(a,b,tol):
    
#     print(f'{'Interation':<15}{'a':<10}{'f(a)':<10}{'b':<10}{'f(b)':<10}{'c':<10}{'f(c)':<10}{'error':<10}')
#     print('-'*80)
    
#     inte=0
#     error=0
#     old_c=a
#     while(True):
          
#           c=(a+b)/2
#           f_a=f_xvalues(a)
#           f_b=f_xvalues(b)
#           f_c=f_xvalues(c)
          
#           error=abs(c-old_c)
          
#           print(f'{inte:<15}{round(a,4):<10}{round(f_a,4):<10}{round(b,4):<10}{round(f_b,4):<10}{round(c,4):<10}{round(f_c,4):<10}{round(error,4):<10}')
    
#           if error<tol:
#               print('Root Is :',c)
#               break
          
#           if f_a*f_c < 0:
#               b=c
#           else:
#               a=c 
                 
#           inte+=1
#           old_c=c
          

# a=1.8
# b=2
# tol=0.01

# bisection(a,b,tol)

# ===================================================================
# ==================================================================
# ====================================================================




# import math

# def f_values(value):
#     return math.pow(value,4)-value- 10   

# def false(a,b,tol):

#     print(f'{'Interation':<15}{'a':<10}{'f(a)':<10}{'b':<10}{'f(b)':<10}{'c':<10}{'f(c)':<10}{'error':<10}')
#     print('-'*80)

#     iter=0
#     old_c=a
    
#     error=0
#     while(True):
#         f_a=f_values(a)
#         f_b=f_values(b)
#         tem1=a*f_b
#         tem2=b*f_a
#         tem3=f_b-f_a
#         c=(a*f_b-b*f_a)/(f_b-f_a)
        
#         f_c=f_values(c)
        
#         error=abs(c-old_c)
        
#         print(f'{iter:<15}{round(a,4):<10}{round(f_a,4):<10}{round(b,4):<10}{round(f_b,4):<10}{round(c,4):<10}{round(f_c,4):<10}{round(error,4):<10}')
    
#         if error<tol:
#             print('Root Is :',round(c,4))
#             break
        
#         if f_a*f_c<0:
#             b=c
#         else:
#             a=c
        
#         iter+=1
#         old_c=c        
            

# a=1.8
# b=2
# tol=0.001

# false(a,b,tol)


    # ====================================================
    # ======================================================
    # ========================================================
    
# import math 
# def f_xvalues(value):
#     return value-math.e**(-value)

# def secand(x0,x1,tol):
    
#     print(f'{'Interation':<15}{'x0':<10}{'f(x0)':<10}{'x1':<10}{'f(x1)':<10}{'x2':<10}{'f(x2)':<10}{'error':<10}')
#     print('-'*80)
    
#     inte=0
#     error=0
#     old_x2=x0
#     while(True):
          
#           f_x0=f_xvalues(x0)
#           f_x1=f_xvalues(x1)
    
#           x2=x1-(f_x1*(x1-x0))/(f_x1-f_x0)
          
#           f_x2=f_xvalues(x2)
          
#           error=abs(x2-old_x2)
#           print(f'{inte:<15}{round(x0,4):<10}{round(f_x0,4):<10}{round(x1,4):<10}{round(f_x1,4):<10}{round(x2,4):<10}{round(f_x2,4):<10}{round(error,4):<10}')
    
#           if error<tol:
#               print('Root Is :',x2)
#               break
          
               
#           inte+=1
#           x0=x1
#           x1=x2
#           old_x2=x2
          

# a=1
# b=2
# tol=0.00001

# secand(a,b,tol)


# *************************************************************************************************
# *************************************************************************************************
# *************************************************************************************************
    
# def f_value(value):
#     return (value**3)-(2*value)-5

# def deriva(value):
#     return 3*(value**2)-2 
    

# def newr(x0,tol):

#     print(f'{'iterations':<15} {'x0':<10} {'f(x0)':<10}{'x1':<10} {'f(x1)':<10} {'error':<10}')
#     print('--'*60)
    
#     iter=0
#     error=0
#     old_x1=x0
#     while(True):
       
#        f_x=f_value(x0)
       
#        f_xd=deriva(x0)
       
#        x1=x0-(f_x/f_xd)
       
#        f_x1=f_value(x1)
       
#        error=abs(x1-old_x1)
#        print(f'{iter:<15} {x0:<10} {f_x:<10}{x1:<10} {f_x1:<10} {error:<10}')
    
#        if error<tol:
#            print('Root Is :',x1)
#            break
       
#        iter+=1     
#        x0=x1
#        old_x1=x1
       
       
# tol=0.0001
# x0=2
# newr(x0,tol)

# *********************************************************************************
# *********************************************************************************

# import math
# def g_x(value):
#     return math.e**(-value)

# def fix(x0,tol):
    
#     error=0
#     gva=0
#     print(f'{'iteration':<15} {'evalues':<10} {'errors':<10}')
#     for i in range(50):
#         gva=g_x(x0)
    
#         error=abs(x0-gva)
        
#         print(f'{i:<15} {round(gva,5):<10} {round(error,5):<10}')
        
#         if(error<tol):
#             print("root is :",gva)
#             break
#         x0=gva
            

    
# x0=1
# tol=0.0001

# fix(x0,tol)



# ********************************************************************
# ********************************************************************


# def lagrange(x,y,value):
#     result=0.0
    
#     n=len(x)
#     for i in range(n):
#         tem=y[i]
#         for j in range(n):
#             if i!=j:
#                 tem*=(value-x[j])/(x[i]-x[j])
        
#         result+=tem        
    
#     return result


# x_point=[-1,1,4,7]
# y_point=[-2,0,63,342]
# f_x=5
# value=lagrange(x_point,y_point,f_x)

# print(round(value,4))


