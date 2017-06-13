#HOMEWORK 2a(ii)-Jacobi
from __future__ import division
import numpy as np
from pandas import DataFrame

def jac(a,b,x,I):
    '''
    function to solve a matrix equation  using Jacobi algorithm
    argument definition:
    a= LHS  Matrix of coefficients
    b= RHS vector
    x= vector of initial guess
    I= number of iterations desired
    '''
    record=[]   #record results of all iterations
    x_new =x[:] #temporal storage of results
    x_rec=x[:]  #hold results for each iteration     
    for t in range(I):
        for i in range(len(b)):
            rowsum = 0
            for j in range(len(b)):
                if j != i:
                    rowsum = rowsum + a[i][j]*x[j]
            x_new[i] = (b[i]-rowsum)/a[i][i]
        x_rec=x_new[:] 
        record.append(x_rec)
        x=x_new[:]   #update solution vector x
    # insert column for iterations in record
    for i in range(I):
        record[i].insert(0,i+1)      
    #create an excel output using pandas
    header =['x{}'.format(i) for i in range(1,len(b)+1)]
    header.insert(0,'Iteration number')
    df = DataFrame(np.array(record),columns=header)
    df.to_excel('Jacobi.xlsx',sheet_name='Jacobi',index=False)
    print df
#code testing
if __name__ == '__main__':
    a1=[[12,7,3],
      [1,5,1],
      [2,7,-11]]
    b1=[22,7,-2]
    x1=[1,2,1]
    #call Jacobi function   
    jac(a1,b1,x1,10)    